# Generated by Django 2.1.2 on 2018-11-19 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0018_auto_20181119_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.DateField(null=True),
        ),
    ]
