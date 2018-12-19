from django.shortcuts import render


def cwp(request):
    html = render(request, 'cwp.html')
    return html