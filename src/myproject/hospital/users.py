from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_user_info']

    def get_user_info(self, obj):
        return "{} {}".format(obj.user.first_name, obj.user.last_name)
