from django.urls import path
from . import views
app_name = 'portfolio'
urlpatterns = [
    path('',views.home,name='home'),
    path('skill',views.skill,name='skill'),
    path('contact-us',views.contactus,name='contactus'),
    path('study',views.study,name='study'),
    path('exprience',views.exprience,name='exprience')
]
