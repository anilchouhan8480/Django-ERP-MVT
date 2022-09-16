from City.models import City_Model
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render
from State.models import State_Model

from .forms import Branch_Forms
from .models import Branch_model

# Create your views here.


@login_required(login_url='/login')
def list(request):
    uObj = State_Model.objects.all()
    cit = City_Model.objects.all()
    data = Branch_model.objects.filter(is_del=False).order_by('Branch_Code')
    paginator = Paginator(data, 20)
    page_number = request.GET.get('page', 1)
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page = Paginator.page(0)
    return render(request, 'Branch_list.html', {'dataFinal': dataFinal, 'uObj': uObj, 'cit': cit})


@login_required(login_url='/login')
def branch_Forms(request):
    if request.method == 'GET':
        form = Branch_Forms()
        return render(request, 'branch.html', {'form': form, })
    else:
        form = Branch_Forms(request.POST)
        if form.is_valid():
            error_count = 0
            branch_Name = form.cleaned_data['Branch_Name']
            if(len(branch_Name) <= 2):
                error_count = error_count+1
                error1 = " Branch Name Must Be of Minimum 3 characters!"
                print("ran into an error")
                form.fields['Branch_Name'].widget.attrs['value'] = ''
                form.fields['Branch_Name'].widget.attrs['placeholder'] = 'Wrong value'
                form.fields['Branch_Name'].widget.attrs['style'] = 'border: 3px solid red'
            if(error_count != 0):
                return render(request, 'branch.html', {'form': form, 'error1': error1, })
            else:
                form.save()
        return redirect('Branch-list')


@login_required(login_url='/login')
def branch_edit_form(request, Branch_Code=0):
    if request.method == 'GET':
        if Branch_Code == 0:
            form = Branch_Forms()

        else:
            data1 = Branch_model.objects.get(Branch_Code=Branch_Code)
            form = Branch_Forms(instance=data1)

        return render(request, 'Branch_Edit.html', {'form': form})
    else:
        if Branch_Code == 0:
            form = Branch_Forms(request.POST)

        else:
            data1 = Branch_model.objects.get(Branch_Code=Branch_Code)
            form = Branch_Forms(request.POST, instance=data1)

        if form.is_valid():
            error_count = 0
            branch_Name = form.cleaned_data['Branch_Name']
            if(len(branch_Name) <= 2):
                error_count = error_count+1
                error1 = " Branch Name Must Be of Minimum 3 characters!"
                print("ran into an error")
                form.fields['Branch_Name'].widget.attrs['value'] = ''
                form.fields['Branch_Name'].widget.attrs['placeholder'] = 'Wrong value'
                form.fields['Branch_Name'].widget.attrs['style'] = 'border: 3px solid red'
            if(error_count != 0):
                return render(request, 'branch.html', {'form': form, 'error1': error1, })
            else:
                form.save()
        return redirect('Branch-list')


@login_required(login_url='/login')
def Branch_Delete(request, Branch_Code):
    data = Branch_model.objects.get(Branch_Code=Branch_Code)
    data.is_del = True
    data.save()
    return redirect('Branch-list')


@login_required(login_url='/login')
def Search_Branch(request):
    title = request.GET['Searchnamebranch']
    data = Branch_model.objects.filter(
        Branch_Name__icontains=title).filter(is_del__icontains=False)
    paginator = Paginator(data, 3)
    page_number = request.GET.get('page', 1)
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page = Paginator.page(0)
    return render(request, 'Branch_list.html', {'dataFinal': dataFinal})
