from django.shortcuts import render, redirect

from .forms import ContactForm
from .models import Contact, ContactMe


def contact(request):
    contact_me = ContactMe.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Forma ma'lumotlarini saqlaydi
            return redirect('.')  # Muvaffaqiyatli yuborilgan sahifaga yo'naltirish
    else:
        form = ContactForm()
    context = {
        "form": form,
        "contact_me": contact_me
    }

    return render(request, 'contact/contact.html', context)
