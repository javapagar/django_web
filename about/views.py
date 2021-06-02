from django.shortcuts import render

def about_me(request):
    context = {
        'nbar':'about'
    }
    return render(request,'aboutme.html', context)
