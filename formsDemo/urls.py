from django.contrib import admin
from django.urls import path
from formsApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userRegistration/', views.userRegistrationView),
]
