from django.shortcuts import render


def cwp(request):
    html = render(request, 'cwp/cwp.html')
    return html