from django.contrib import admin
from .models import Esrog

print(f"esrogim == {Esrog.objects.all()}")


admin.site.register(Esrog)

# Register your models here.
