from django.urls import path
from .views import main,contact,products,single_product,about

urlpatterns = [
    path('',main),
    path('about/',about),
    path('contact/',contact),
    path('products/',products),
    path('singleproduct/',single_product),
]