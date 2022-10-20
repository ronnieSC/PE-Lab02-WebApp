from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.

def send(request, myID):
    usr = User.objects.filter(id=myID).get()
    print('-----------------------------')
    print(usr)
    print('-----------------------------')
    cabecera = 'Empresa MinimarketPWEB2'
    mensaje = 'Bienvenido a la empresa:\nSu usuario de acceso es: '+usr.username+'\nsu contraseña es: '+usr.password
    origen = 'minim8475@gmail.com'
    send_mail(cabecera, mensaje, origen, [usr.email], fail_silently=False)
    return render(request, 'send.html')