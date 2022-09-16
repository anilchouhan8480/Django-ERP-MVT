from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render

from .forms import PoLine_Form
from .models import PoLine_Model
from django.contrib.auth.decorators import login_required
@login_required(login_url='/login')

# Create your views here.
@login_required(login_url='/login')
def PoLine_list(request):
    data = PoLine_Model.objects.all()
    return render(request, 'PoLine_List.html',{'data': data})

@login_required(login_url='/login')
def poLine_Form(request):
    if request.method == 'GET':
        form = PoLine_Form()
        return render(request, 'PoLine_Create.html',{'form': form})

    else:
        form = PoLine_Form(request.POST)
        if form.is_valid():
           
                form.save()
        return redirect('PoLine-list')

@login_required(login_url='/login')
def PoLine_edit_form(request,  PoLine_No=0):
    if request.method == 'GET':
        if  PoLine_No == 0:
            form = PoLine_Form()

        else:
            data1 = PoLine_Model.objects.get( PoLine_No= PoLine_No)
            form = PoLine_Form(instance=data1)
        return render(request, 'PoLine_Edit.html', {'form': form})
    else:
        if  PoLine_No == 0:
            form = PoLine_Form(request.POST)

        else:
            data1 = PoLine_Model.objects.get(PoLine_Code= PoLine_No)
            form = PoLine_Form(request.POST, instance=data1)

        if form.is_valid():
           
                form.save()
        return redirect('PoLine-list')

@login_required(login_url='/login')
def PoLine_Delete(request, PoLine_Code):
    data = PoLine_Model.objects.get(PoLine_Code=PoLine_Code)
    data.is_del = True
    data.save()
    return redirect('PoLine-list')


@login_required(login_url='/login')
def search_PoLine(request):
    title = request.GET['Searchpoline']
    data = PoLine_Model.objects.filter(
        PoLine_No__icontains=title).filter(is_del__icontains=False)
    paginator = Paginator(data, 3)
    page_number = request.GET.get('page', 1)
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page = Paginator.page(0)
    return render(request, 'PoLine_List.html', {'dataFinal': dataFinal})
