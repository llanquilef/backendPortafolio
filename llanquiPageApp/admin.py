from django.contrib import admin
from .models import RecomendacionPersonal, RecomendacionUsuario, Emails

# ====== RECOMENDACIÓN USUARIO ADMIN / PERSONAL USER ADMIN ======
admin.site.register(RecomendacionUsuario)

# ====== RECOMENDACIÓN PERSONAL ADMIN / PERSONAL RECOMENDATION ADMIN ======
admin.site.register(RecomendacionPersonal)

# ====== EMAIL ADMIN ======
admin.site.register(Emails)
