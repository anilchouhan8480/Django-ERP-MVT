from django.shortcuts import render


def inventory_list(request):
    return render(request, 'inventory_list.html', {'data': {}})


def stock_details(request):
    return render(request, 'stock_details.html', {'data': {}})


def stock_details_create(request):
    return render(request, 'stock_details_create.html', {'data': {}})


def stock_history(request):
    return render(request, 'stock_history.html', {'data': {}})
