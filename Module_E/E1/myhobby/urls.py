from django.urls import path
from. import views
from .views import PageHome, about, contact

urlpatterns = [
    path('', PageHome.as_view(), name='home'),#главная страница
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]