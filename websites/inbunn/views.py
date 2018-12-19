from django.shortcuts import render


def emily(request):
    html = render(request, 'inbunn/emily.html')
    return html