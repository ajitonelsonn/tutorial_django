from django.shortcuts import render

# Create your views here.
def contact(request):
    context={
        'naran': 'Hau nia contact',
    }
    return render(request, 'contact/contact.html', context)