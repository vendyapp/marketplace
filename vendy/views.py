from django.shortcuts import render


def index(request):
    context_dict = {}
    template = 'index.html'

    return render(request, template, context=context_dict)


def bids(request):
    context_dict = {}
    template = 'bids.html'

    return render(request, template, context=context_dict)


def manage(request):
    context_dict = {}
    template = 'manage.html'

    return render(request, template, context=context_dict)


def breezer_f400(request):
    context_dict = {}
    template = 'breezer_f400.html'

    return render(request, template, context=context_dict)