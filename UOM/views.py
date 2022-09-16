from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render

from .forms import UOM_Forms
from .models import UOM_model


# Create your views here.
@login_required(login_url='/login')
def list(request):
    data = UOM_model.objects.filter(is_del=False).order_by('UOM_NO')
    paginator = Paginator(data, 20)
    page_number = request.GET.get('page', 1)
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page = Paginator.page(0)
    return render(request, 'unit_of_measure_list.html', {'dataFinal': dataFinal, })


@login_required(login_url='/login')
def UOM_forms(request):
    if request.method == 'GET':
        form = UOM_Forms()
        return render(request, 'unit_of_measure.html', {'form': form})

    else:
        form = UOM_Forms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('unitofmeasure-list')


@login_required(login_url='/login')
def uom_edit_form(request, UOM_NO=0):
    if request.method == 'GET':
        if UOM_NO == 0:
            form = UOM_Forms()

        else:
            data1 = UOM_model.objects.get(UOM_NO=UOM_NO)
            form = UOM_Forms(instance=data1)

        return render(request, 'UOM_EDIT.html', {'form': form})
    else:
        if UOM_NO == 0:
            form = UOM_Forms(request.POST)

        else:
            data1 = UOM_model.objects.get(UOM_NO=UOM_NO)
            form = UOM_Forms(request.POST, instance=data1)

        if form.is_valid():
            form.save()
            return redirect('unitofmeasure-list')


@login_required(login_url='/login')
def UOM_Delete(request, UOM_NO):
    data = UOM_model.objects.get(UOM_NO=UOM_NO)
    data.is_del = True
    data.save()
    return redirect('unitofmeasure-list')


@login_required(login_url='/login')
def Search_UOM(request):
    title = request.GET['Searchnameuom']
    data = UOM_model.objects.filter(
        UOM__icontains=title).filter(is_del__icontains=False)
    paginator = Paginator(data, 3)
    page_number = request.GET.get('page', 1)
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page = Paginator.page(0)
    return render(request, 'unit_of_measure_list.html', {'dataFinal': dataFinal})
