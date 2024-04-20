from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

@login_required()
def hello(request):  # request semnaleaza faptul ca functia este apelata pe baza unui url, in urls.py
    return HttpResponse("<h1>Hello, World!</h1>")


@login_required()
def hello_again(request):
    return HttpResponse("Hello, again!")


@login_required()
def cars(request):
    context = {
        'all_cars': [
            {
                'name_of_brand': 'Tesla',
                'model': 'Model Y',
                'color': 'white',
                'year': 2024
            },
            {
                'name_of_brand': 'Dacia',
                'model': 'Spring',
                'color': 'blue',
                'year': 2023
            },
            {
                'name_of_brand': 'Ford',
                'model': 'Mach E',
                'color': 'purple',
                'year': 2025
            }
        ]
        # ,
        # 'all_people': [
        #     {
        #
        #     }
        # ]
    }

    return render(request, 'intro/list_of_cars.html', context)


# definiti o functie noua in care sa trimiteti carti/filme/muzica, cu 4-5 dictionare in listaa -nume/gen/etc,
# creare functie, path si pagina html

@login_required()
def songs(request):
    context_songs = {
        'all_songs': [
            {
                'song_title': 'Whatever',
                'song_artist': 'Somebody',
                'song_year': 2027
            },
            {
                'song_title': 'La La La',
                'song_artist': 'Nobody',
                'song_year': 1
            }
        ]
    }
    return render(request, 'intro/list_of_songs.html', context_songs)
