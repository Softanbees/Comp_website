from django.urls import path
from .views import home, send_info, send_email

# app_name = 'apply'

urlpatterns = [
    path('',home,name='apply'),
    path('send_info/',send_info, name = "send_info"),
    path('send_only_email/',send_email, name = "send_only_email"),

]
