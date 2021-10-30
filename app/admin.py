from django.contrib import admin
from .models import Days, Time, Doctors


admin.site.register(Days)
admin.site.register(Doctors)
admin.site.register(Time)