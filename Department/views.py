from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render

from .forms import Department_Forms
from .models import Department_model


# Create your views here.
@login_required(login_url='/login')
def list(request):
    data = Department_model.objects.filter(
        is_del=False).order_by('Department_Code')
    paginator = Paginator(data, 20)
    page_number = request.GET.get('page', 1)
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page = Paginator.page(0)
    return render(request, 'department_list.html', {'dataFinal': dataFinal, })

@login_required(login_url='/login')
def Department_forms(request):
    if request.method == 'GET':
        form = Department_Forms()
        return render(request, 'department_create.html', {'form': form})

    else:
        form = Department_Forms(request.POST)
        if form.is_valid():
            error_count = 0
            Department_Name = form.cleaned_data['Department_Name']
            if(len(Department_Name) <= 2):
                error_count = error_count+1
                error1 = " Department Name Must Be of Minimum 3 characters!"
                print("ran into an error")
                form.fields['Department_code'].widget.attrs['value'] = ''
                form.fields['Department_code'].widget.attrs['placeholder'] = 'Wrong value'
                form.fields['Department_code'].widget.attrs['style'] = 'border: 3px solid red'
            if(error_count != 0):
                return render(request, 'department_create.html', {'form': form, 'error1': error1, })
            else:
                form.save()
        return redirect('department-list')

@login_required(login_url='/login')
def department_edit_form(request, Department_Code=0):
    if request.method == 'GET':
        if Department_Code == 0:
            form = Department_Forms()

        else:
            data1 = Department_model.objects.get(Department_Code=Department_Code)
            form = Department_Forms(instance=data1)
        return render(request, 'department_edit.html', {'form': form})
    else:
        if Department_Code == 0:
            form = Department_Forms(request.POST)

        else:
            data1 = Department_model.objects.get(Department_Code=Department_Code)
            form = Department_Forms(request.POST, instance=data1)
            if form.is_valid():
                error_count = 0
                department_Name = form.cleaned_data['Department_Name']
                if(len(department_Name) <= 2):
                    error_count = error_count+1
                    error1 = " Department Name Must Be of Minimum 3 characters!"
                    print("ran into an error")
                    form.fields['Department_Name'].widget.attrs['value'] = ''
                    form.fields['Department_Name'].widget.attrs['placeholder'] = 'Wrong value'
                    form.fields['Department_Name'].widget.attrs['style'] = 'border: 3px solid red'
                if(error_count != 0):
                    return render(request, 'department_create.html', {'form': form, 'error1': error1, })
                else:
                    form.save()
    return redirect('department-list')

@login_required(login_url='/login')
def dep_Delete(request, Department_Code):
    data = Department_model.objects.get(Department_Code=Department_Code)
    data.is_del = True
    data.save()
    return redirect('department-list')

@login_required(login_url='/login')
def Search_dep(request):
    title = request.GET['Searchdep']
    data = Department_model.objects.filter(
        Department_Name__icontains=title).filter(is_del__icontains=False)
    paginator = Paginator(data, 3)
    page_number = request.GET.get('page', 1)
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page = Paginator.page(0)
    return render(request, 'department_list.html', {'dataFinal': dataFinal})
