from django.shortcuts import render

# Create your views here.
def index (request):
    context= {
        'naran': 'Hello World !'
    }
    return render(request, 'index.html', context)