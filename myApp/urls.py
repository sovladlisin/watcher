from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'myApp'
urlpatterns = [
    path('addPatient', views.AddUser, name='addPatient'),
    path('user/logPatient', views.UserPatientLog, name='listPatientUser'),

    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),

    path('admin/logPatient', views.AdminPatientLog, name='logPatientAdmin'),
    path('admin/allPatient', views.AdminPatientAll, name='allPatientAdmin'),
    path('admin/activations', views.getNewActivations, name='activations'),
    path('admin/allUser', views.AdminUserAll, name='allUserAdmin'),

    url(r'^patient/(?P<pk>\d+)/edit/$', views.PatientEdit, name='patientEdit'),
    url(r'^patient/(?P<pk>\d+)/answer/$', views.PatientAnswer, name='patientAnswer'),
    url(r'^patient/(?P<pk>\d+)/delete/$', views.AdminPatientDelete, name='patientDelete'),
]

# url(r'^user/listPatient/$', PatientFiletView.as_view(filterset_class=PatientFilter,
# #                                      template_name='myApp/user_list.html'), name='search'),