from django.shortcuts import render
from .models import Contacto
from django.conf import settings
from django.core.mail import EmailMultiAlternatives, send_mail
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

@login_required
def projects(request):
    response = {}
    if request.method == "POST":
        data = request.POST

        contacto_val = Contacto()
        contacto_val.nombre = data['name']
        contacto_val.email = data['email']
        contacto_val.telefono = data['phone']
        contacto_val.mensaje = data['message']
        contacto_val.save()

        email_html('Bienvenido!', data)

        return HttpResponseRedirect('/exitoso/')
    return render(request, 'contactos.html', context=response)

@login_required
def success(request):
    return render(request, 'exitoso.html', context={})

def email_html(subject, data):
    html_message = ('<div style="font-family: sans-serif; text-align:center; border: 1px solid #412378; margin-top: 30px;max-width: 550px;margin: 0 auto;">' +
            '<div style="background-color: #a90a59; padding:5px;">' +
                '<h1>Contacto nuevo</h1>' +
            '</div>' +
            '<div style="padding:20px; font-size:16px;">' +
                'Se has registrado como contacto - '+ data['name'] + 
                ', con el correo' + data['email'] + '.<br>' +
                'Teléfono: ' + str(data['phone']) + '.<br>' + 
                'Mensaje: ' + str(data['message']) + '<br>' + 
            '</div>' +
        '</div>'
    )
    from_email = settings.EMAIL_HOST_USER
    send_mail(
        subject=subject,
        message='',
        html_message=html_message,
        from_email=from_email,
        recipient_list=['josecheche14@gmail.com']
    )