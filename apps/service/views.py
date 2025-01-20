from django.shortcuts import render
from .models import Service


def service(request):
    service_obj = Service.objects.all()
    context = {
        'services': service_obj,
    }
    return render(request, 'service/service.html', context)
