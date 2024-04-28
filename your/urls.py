from django.urls import path
from .views import home_view,contact_view,news_view,products_view,services_view
urlpatterns = [
    path('', home_view, name="home-page"),
    path('contact/', contact_view, name="contact-page"),
    path('news/', news_view, name="news-page"),
    path('products/', products_view, name="products-page"),
    path('services/', services_view, name="services-page"),
]