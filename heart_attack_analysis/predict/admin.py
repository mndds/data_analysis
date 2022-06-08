from django.contrib import admin
from .models import Prediction

# Register your models here.

class PredictionAdmin(admin.ModelAdmin):
    list_display = ['id','fullname','cvd','cvd_non','created_at']
    list_display_links = ['id','fullname']
    search_fields = ['fullname']

admin.site.register(Prediction,PredictionAdmin)
