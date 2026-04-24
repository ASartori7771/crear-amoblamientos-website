from django.shortcuts import redirect, render
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm


def inicio(request):
    return render(request, 'core/inicio.html')


def contacto(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            full_message = f"""
Nombre: {data['from_name']}
Email: {data['reply_to']}

Mensaje:
{data['message']}
"""

            try:
                email = EmailMessage(
                    subject=data['title'],
                    body=full_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[settings.TO_EMAIL],
                    reply_to=[data['reply_to']],
                )

                email.send()

                messages.success(request, "Mensaje enviado correctamente ✅")
                return redirect("contacto")

            except Exception as e:
                print("EMAIL ERROR:", e)
                messages.error(request, "Error al enviar el mensaje ❌")

        else:
            messages.error(request, "Por favor completa correctamente el formulario ⚠️")

    else:
        form = ContactForm()

    return render(request, "core/contacto.html", {"form": form})


def informacion(request):
    return render(request, 'core/informacion.html')
