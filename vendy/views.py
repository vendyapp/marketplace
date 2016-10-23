from django.shortcuts import render


def index(request):
    context_dict = {}
    template = 'index.html'

    return render(request, template, context=context_dict)


def bids(request):
    context_dict = {}
    template = 'bids.html'

    return render(request, template, context=context_dict)