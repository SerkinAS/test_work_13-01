from django.contrib import admin
from . import models


# Зарегистрируем в админке наши модели.
admin.site.register(models.Employee)
admin.site.register(models.Group)
