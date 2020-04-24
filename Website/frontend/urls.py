from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('results', views.results, name = "results"),
    path('predict', views.predict, name = "predict"),
    path('find', views.findPlayer, name = "findPlayer")
]
