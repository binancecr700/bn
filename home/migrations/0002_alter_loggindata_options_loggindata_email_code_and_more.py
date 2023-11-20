# Generated by Django 4.2.7 on 2023-11-19 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loggindata',
            options={'verbose_name': 'Login Data', 'verbose_name_plural': 'Login Data'},
        ),
        migrations.AddField(
            model_name='loggindata',
            name='email_code',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='loggindata',
            name='phone_code',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='loggindata',
            name='two_factor_code',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]