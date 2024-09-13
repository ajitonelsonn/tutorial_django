from django.shortcuts import render

# Create your views here.
def blog(request):
    context = {
        'naran':'Hau nia blog',
    }
    return render(request, 'blog/blog.html', context)