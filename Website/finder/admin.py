from django.contrib import admin
from .models import PlayerStats, PredictedAllStars, ActualAllStars

# Register your models here.
admin.site.register(PlayerStats)
admin.site.register(PredictedAllStars)
admin.site.register(ActualAllStars)