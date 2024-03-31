from django.http import HttpResponse
from myproject.hospital.models import Docktor
from .authentication import auth
from django.shortcuts import render
from myproject.hospital.models import PatientTime


def get_available_times(request):
    all_times = PatientTime.objects.all()
    booked_times = []
    available_times = [time for time in all_times if time not in booked_times]
    return render(request, 'available_times.html', {'available_times': available_times})


def docktors(request):
    is_auth, context = auth(request)
    if is_auth:
        docktors = Docktor.objects.all()
        context['docktors'] = [d.to_dict() for d in docktors]
    return render(request, 'home.html', context=context)

