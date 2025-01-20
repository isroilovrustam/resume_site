from django.shortcuts import render
from .models import About, Education, Experience


def index(request):
    about_obj = About.objects.all()
    context = {
        "about": about_obj,
    }
    return render(request, "index/index.html", context)


def about(request):
    about_obj = About.objects.all()
    edu_obj = Education.objects.all()
    exp_obj = Experience.objects.all()
    context = {
        "about": about_obj,
        "education": edu_obj,
        "experience": exp_obj,
    }
    return render(request, "about/about.html", context)


def credential(request):
    about_obj = About.objects.all()
    edu_obj = Education.objects.all()
    exp_obj = Experience.objects.all()
    context = {
        "about": about_obj,
        "education": edu_obj,
        "experience": exp_obj,
    }
    return render(request, "about/credentials.html", context)
