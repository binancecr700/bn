# Generated by Django 4.2.7 on 2023-11-19 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_loggindata_options_loggindata_email_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loggindata',
            name='otp',
        ),
    ]
