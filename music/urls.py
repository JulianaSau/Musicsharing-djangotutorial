from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
	# /music/
    path('', views.index, name='index'),

    # /music/[album_id]/
    #path(r'^(?p<album_id>[0-9]+)/$', views.detail, name="detail"),
    path('<int:album_id>/', views.detail, name="detail"),
]