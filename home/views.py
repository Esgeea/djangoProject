from django.shortcuts import render
from django.views.generic import TemplateView


# TemplateView -> randarea unei pagini HTML

# clasa dezvoltata de Django pentru a afisa un sablon, o pagina HTML

# caracteristici:
# 1. manipulare sabloane: este proiectat pentru a lucra cu pagini .html in care puteti sa specificati template-ul dorit pentru afisarea continutului
# 2. gestionare context: puteti sa furnizati context suplimentar pentru template, permitand trimiterea de variabile si informatii

class HomeTemplateView(TemplateView):   # mosteneste clasa de Django care are si variabile predefinite (template_name)
    template_name = 'home/homepage.html'   # specificare fisier html pentru care se doreste randare/afisare

