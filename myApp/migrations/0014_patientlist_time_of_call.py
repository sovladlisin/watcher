# Generated by Django 2.1.2 on 2018-11-19 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0013_auto_20181107_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientlist',
            name='time_of_call',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
