from rest_framework import viewsets
from .models import RecomendacionPersonal, RecomendacionUsuario
from .serializers import RecomendacionPersonalSerializer, RecomendacionUsuarioSerializer, UsuarioSerializer
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.views.generic.edit import FormView
from .forms import EmailForm

# ====== USUARIOS / USERS ======

class UserViewSet(viewsets.ModelViewSet):
    """
    Vista que permite apuntar al registro de mis rutas de la API para visualizar mis recomendaciones personales.
    """
    queryset = User.objects.all()  # Consulta para obtener todos los usuarios
    serializer_class = UsuarioSerializer  # Serializador utilizado para los usuarios

# ====== RECOMENDACIÓN PERSONAL / PERSONAL RECOMENDATION ======

class R_PersonalViewSet(viewsets.ModelViewSet):
    """
    Vista que permite apuntar al registro de mis rutas de la API para visualizar mis recomendaciones personales.
    """
    queryset = RecomendacionPersonal.objects.all()  # Consulta para obtener todas las recomendaciones personales
    serializer_class = RecomendacionPersonalSerializer  # Serializador utilizado para las recomendaciones personales

# RECOMENDACIÓN USUARIO / USER RECOMENDATION

class R_UsuarioViewSet(viewsets.ModelViewSet):
    """
    Vista que permite apuntar al registro de mis rutas de la API para visualizar las recomendaciones de los usuarios de la página.
    """
    queryset = RecomendacionUsuario.objects.all()  # Consulta para obtener todas las recomendaciones de los usuarios
    serializer_class = RecomendacionUsuarioSerializer  # Serializador utilizado para las recomendaciones de los usuarios

class EmailCreateView(FormView):
    """
    Vista basada en formularios para crear y enviar correos electrónicos.
    """
    template_name = "email.html"  # Plantilla utilizada para renderizar el formulario
    form_class = EmailForm  # Formulario utilizado para crear el correo electrónico
    success_url = "/"  # URL a la que redirigir después de enviar el formulario con éxito

    def form_valid(self, form):
        """
        Método llamado cuando el formulario es válido. Guarda la instancia del correo electrónico y envía el correo.
        """
        email_instance = form.save(commit=False)  # Guarda la instancia del formulario sin enviarla a la base de datos
        email_instance.subject = "Nuevo mensaje desde tu aplicación"  # Asigna el asunto del correo
        email_instance.message = "Email Django funcionando"  # Asigna el mensaje del correo
        email_instance.save()  # Guarda la instancia del correo en la base de datos

        # Lógica para enviar el correo
        send_mail(
            subject=email_instance.subject,
            message=email_instance.message,
            from_email=email_instance.email,  # Email del remitente
            recipient_list=[email_instance.email],  # Destinatarios
            fail_silently=False,
        )

        return super().form_valid(form)  # Llama al método form_valid del padre para continuar con el flujo normal