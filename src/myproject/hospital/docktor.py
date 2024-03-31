from django.db import models
from django.contrib import admin
from myproject.hospital.patienttime import PatientTime

class Docktor(models.Model):
    name = models.CharField(max_length=16)
    surname = models.CharField(max_length=16)
    profession = models.CharField(max_length=16)
    time_for_patient = models.ManyToManyField(PatientTime)

    def __str__(self):
        return "{} {} {}".format(self.name, self.surname, self.profession)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'profession': self.profession
        }


@admin.register(Docktor)
class DocktorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'profession']
