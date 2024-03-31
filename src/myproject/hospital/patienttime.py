from django.db import models
from django.contrib import admin
from myproject.hospital.users import Patient
from datetime import time, timedelta


class PatientTime(models.Model):
    time = models.DateTimeField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return self.time.strftime("%Y-%m-%d %H:%M:%S")


    def available_times(self):
        start_time = time(9, 0)
        end_time = time(18, 0)
        interval = timedelta(minutes=30)

        current_time = start_time
        time_slots = []

        while current_time < end_time:
            time_slots.append(current_time.strftime('%H:%M'))
            current_time += interval

        return time_slots


@admin.register(PatientTime)
class PatientTimeAdmin(admin.ModelAdmin):
    list_display = ['id', 'time', 'available_times']
