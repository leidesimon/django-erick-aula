from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def index(request):
    context = {
        'nomes':[
            'Eric'
            'Fagner'
            'Camila'
            'Fayra'
        ],
        


# Create your views here.
