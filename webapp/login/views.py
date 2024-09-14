from django.shortcuts import render

# Create your views here.
def login_views(request):
    context={}
    return render(request, 'login/login_view.html', context)