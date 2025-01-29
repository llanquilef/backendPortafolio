# Portafolio Personal - Backend
Backend del portafolio personal desarrollado con Django. Proporciona una API RESTful para gestión de recomendaciones multimedia y sistema de notificación de errores.

## ✨ Características Clave
- **Gestión de Recomendaciones**
  - CRUD completo para recomendaciones personales y de usuarios
  - Sistema de categorización multimedia
- **Manejo de Errores**
  - Notificación automática de errores vía email
  - Registro detallado en logs

## 🚀 Stack Tecnológico
| Capa               | Tecnologías                                                                  |
|-----------------   | -----------------------------------------------------------------------------|
| **Framework**      | Django 4.2 + Django REST Framework 3.14                                      |
| **Base de Datos**  | PostgreSQL 15 + psycopg2                                                     |
| **Seguridad**      | CORS Headers, Django-environ, Rate Limiting                                  | 
| **Infra**          | Whitenoise (static files), Gunicorn (production WSGI), Nginx (reverse proxy) |
| **Monitorización** | Sentry (error tracking), Prometheus + Grafana (métricas)                     |

## 🛠️ Instalación Local
1. Clonar repositorio:
```bash
git clone https://github.com/llanquilef/portafolioDjango.git