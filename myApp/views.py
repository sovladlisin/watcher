import simplejson as simplejson
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
import json
from django.http import StreamingHttpResponse, HttpResponseRedirect, HttpResponse
import django_filters
from django import forms
import datetime
from myApp.forms import UserProfileInfoForm, UserForm, PatientForm
from myApp.models import Patient, PatientList, Wing, PatientLog, UserProfileInfo
from django.views.decorators.csrf import csrf_exempt


@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    # return HttpResponseRedirect(reverse('index'))

def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.is_active = False
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('myApp:allPatientAdmin')
        else:
            mark = True
            return render(request,'myApp/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,'mark':mark
                           })
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'myApp/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           })

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                if UserProfileInfo.objects.get(user=user).is_admin:
                    return redirect('myApp:allPatientAdmin')
                if UserProfileInfo.objects.get(user=user).is_doctor:
                    return redirect('myApp:listPatientUser')
            else:
                return render(request, 'myApp/loginError.html', {})
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return render(request, 'myApp/loginError.html', {})
    else:
        return render(request,'myApp/login.html', {})

def user_login_error(request):
    return render(request, 'myApp/login.html', {})

def AdminPatientDelete(request,pk):
    Patient.objects.get(pk=pk).delete()
    return redirect('myApp:logPatientAdmin')

class PatientFilter(django_filters.FilterSet):
    # Patient.name = django_filters.CharFilter(lookup_expr='icontains')
    patient__wing = django_filters.ModelMultipleChoiceFilter(queryset=Wing.objects.all(),
                                                      widget=forms.CheckboxSelectMultiple)
    patient__surname = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = PatientList
        fields = {
            'patient__name',
            'patient__surname',
            'patient__wing'
        }

def UserPatientLog(request):
    if request.user.is_authenticated:
        marker = False
        if UserProfileInfo.objects.get(user=request.user).is_admin:
            marker = True
        patient_log = PatientList.objects.all()
        patient_filter = PatientFilter(request.GET, queryset=patient_log)
        return render(request, 'myApp/user/logPatient.html',
                      {'patient_log': patient_log, 'patient_filter': patient_filter, 'marker': marker})
    else:
        return redirect('myApp:user_login')


def AdminPatientAll(request):
    if request.user.is_authenticated:
        if UserProfileInfo.objects.get(user=request.user).is_admin:
            patient_list = Patient.objects.all().exclude(name='Не указано')
            return render(request, 'myApp/admin/allPatient.html', {'patient_list': patient_list})
        else:
            return render(request, 'myApp/authError.html')
    else:
        return redirect('myApp:user_login')

def AdminUserAll(request):
    if request.user.is_authenticated:
        if UserProfileInfo.objects.get(user=request.user).is_admin:
            user_list = UserProfileInfo.objects.all().exclude(user__is_active=False)
            new_user_list = UserProfileInfo.objects.all().exclude(user__is_active=True)
            return render(request, 'myApp/admin/allUser.html', {'user_list': user_list, 'new_user_list': new_user_list })
        else:
            return render(request, 'myApp/authError.html')
    else:
        return redirect('myApp:user_login')

def AdminPatientLog(request):
    if request.user.is_authenticated:
        if UserProfileInfo.objects.get(user=request.user).is_admin:
            patient_log = PatientList.objects.all()
            patient_unknown = Patient.objects.filter(name='Не указано')
            return render(request, 'myApp/admin/logPatient.html',
                          {'patient_log': patient_log, 'patient_unknown': patient_unknown})
        else:
            return render(request, 'myApp/authError.html')
    else:
        return redirect('myApp:user_login')




def PatientEdit(request, pk):
    if request.user.is_authenticated:
        patient = get_object_or_404(Patient, pk=pk)

        current_patient = Patient.objects.get(pk=pk)
        if request.method == "POST":
            form = PatientForm(request.POST, instance=patient)
            if form.is_valid():
                patient = form.save(commit=False)
                patient.save()
                return redirect('myApp:allPatientAdmin')
            else:
                return HttpResponse("Ошибка в форме")
        else:
            form = PatientForm(instance=patient)
        return render(request, 'myApp/admin/patientEdit.html', {'form': form, 'current': current_patient})
    else:
        return redirect('myApp:user_login')

# removing line from calls by doctor pressing the button

def PatientAnswer(request, pk):
    now = datetime.datetime.now()
    pk_patient = get_object_or_404(PatientList, pk=pk).patient.pk
    patient = get_object_or_404(Patient, pk=pk_patient)
    patient_call_time = get_object_or_404(PatientList, pk=pk).time_of_call
    PatientLog(patient=patient, time_of_call=patient_call_time, worker=request.user, time_of_answer=now).save()
    get_object_or_404(PatientList, pk=pk).delete()
    if UserProfileInfo.objects.get(user=request.user).is_admin:
        return redirect('myApp:allPatientAdmin')
    if UserProfileInfo.objects.get(user=request.user).is_doctor:
        return redirect('myApp:listPatientUser')


# updating calls from patients
@csrf_exempt
def getNewActivations(request):
    if request.method == 'GET':
        patient_unknown = Patient.objects.filter(name='Не указано')
        calls = PatientList.objects.count()
        new_users = UserProfileInfo.objects.all().exclude(user__is_active=True).count()
        new_activations = patient_unknown.count()
        response = {}
        template = render_to_string('myApp/admin/activations.html', {'patient_unknown': patient_unknown})
        response['template'] = template
        response['calls'] = calls
        response['new_users'] = new_users
        response['new_activations'] = new_activations

        return HttpResponse(json.dumps(response))


@csrf_exempt
def AddUser(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body.decode("utf-8"))
        id = str(received_json_data)
        # Patient(z_id=id).save()
        if Patient.objects.filter(z_id=id).count() == 0:
            p = Patient(z_id=id).save()
        else:
            if PatientList.objects.filter(patient=Patient.objects.filter(z_id=id).first()).count() == 0:
                if Patient.objects.filter(z_id=id).first().name != 'Не указано':
                    p = Patient.objects.filter(z_id=id).first()
                    PatientList(patient=p, time_of_call=datetime.datetime.now()).save()

        return StreamingHttpResponse('' + str(received_json_data))
    return StreamingHttpResponse('it was GET request')






