from django.urls import path

from intro import views

# fiecare url poate apela o singura functie sau o singura clasa
# daca doua paths sunt identice, doar primul path va fi considerat
urlpatterns = [
    path('first_page/', views.hello, name='first_func'),
    path('second_page/', views.hello_again, name='first_func'),
    path('list_cars/', views.cars, name='list-cars'),
    path('list_songs/', views.songs, name='list-songs'),
]