from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render

from .forms import Gst_Forms
from .models import Gst_Model


# Create your views here.
@login_required(login_url='/login')
def list(request):
    data = Gst_Model.objects.filter(is_del=False).order_by('Gst_Code')
    paginator = Paginator(data, 20)
    page_number = request.GET.get('page', 1)
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page = Paginator.page(0)
    return render(request, 'gstlist.html', {'dataFinal': dataFinal, })


@login_required(login_url='/login')
def gst_forms(request):
    if request.method == 'GET':
        form = Gst_Forms()
        return render(request, 'gst.html', {'form': form})

    else:
        form = Gst_Forms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('gst-list')


@login_required(login_url='/login')
def gst_edit_form(request, Gst_Code=0):
    if request.method == 'GET':
        if Gst_Code == 0:
            form = Gst_Forms()

        else:
            data1 = Gst_Model.objects.get(Gst_Code=Gst_Code)
            form = Gst_Forms(instance=data1)
        return render(request, 'gst_edit.html', {'form': form})
    else:
        if Gst_Code == 0:
            form = Gst_Forms(request.POST)

        else:
            data1 = Gst_Model.objects.get(Gst_Code=Gst_Code)
            form = Gst_Forms(request.POST, instance=data1)

        if form.is_valid():
            form.save()
            return redirect('gst-list')


@login_required(login_url='/login')
def gst_Delete(request, Gst_Code):
    data = Gst_Model.objects.get(Gst_Code=Gst_Code)
    data.is_del = True
    data.save()
    return redirect('gst-list')


@login_required(login_url='/login')
def search_GST(request):
    title = request.GET['Searchgst']
    data = Gst_Model.objects.filter(
        Gst__icontains=title).filter(is_del__icontains=False)
    paginator = Paginator(data, 3)
    page_number = request.GET.get('page', 1)
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page = Paginator.page(0)
    return render(request, 'gstlist.html', {'dataFinal': dataFinal})
