from django.shortcuts import render


def resume(request):
    html = render(request, 'nick/index.html')
    return html