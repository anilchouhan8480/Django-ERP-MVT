from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render

from .forms import Category_form
from .models import Category_Model


# Create your views here.
@login_required(login_url='/login')
def list(request):
    data = Category_Model.objects.filter(is_del=False).order_by('Category_NO')
    paginator = Paginator(data, 20)
    page_number = request.GET.get('page', 1)
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page = Paginator.page(0)
    return render(request, 'Category_list.html', {'dataFinal': dataFinal, })

@login_required(login_url='/login')
def category_forms(request):
    if request.method == 'GET':
        form = Category_form()
        return render(request, 'Category_Create.html', {'form': form})

    else:
        form = Category_form(request.POST)
        if form.is_valid():
            error_count = 0
            category_Name = form.cleaned_data['Category_Name']
            if(len(category_Name) <= 2):
                error_count = error_count+1
                error1 = "Category Name Must Be of Minimum 3 characters!"
                print("ran into an error")
                form.fields['Category_Name'].widget.attrs['value'] = ''
                form.fields['Category_Name'].widget.attrs['placeholder'] = 'Wrong value'
                form.fields['Category_Name'].widget.attrs['style'] = 'border: 3px solid red'
            if(error_count != 0):
                return render(request, 'Category_Create.html', {'form': form, 'error1': error1, })
            else:
                form.save()
        return redirect('category-list')

@login_required(login_url='/login')
def category_edit_form(request, Category_NO=0):
    if request.method == 'GET':
        if Category_NO == 0:
            form = Category_form()

        else:
            data1 = Category_Model.objects.get(Category_NO=Category_NO)
            form = Category_form(instance=data1)
        return render(request, 'Category_edit.html', {'form': form})
    else:
        if Category_NO == 0:
            form = Category_form(request.POST)

        else:
            data1 = Category_Model.objects.get(Category_NO=Category_NO)
            form = Category_form(request.POST, instance=data1)

        if form.is_valid():
            error_count = 0
            category_Name = form.cleaned_data['Category_Name']
            if(len(category_Name) <= 2):
                error_count = error_count+1
                error1 = "Category Name Must Be of Minimum 3 characters!"
                print("ran into an error")
                form.fields['Category_Name'].widget.attrs['value'] = ''
                form.fields['Category_Name'].widget.attrs['placeholder'] = 'Wrong value'
                form.fields['Category_Name'].widget.attrs['style'] = 'border: 3px solid red'
            if(error_count != 0):
                return render(request, 'Category_edit.html', {'form': form, 'error1': error1, })
            else:
                form.save()
            return redirect('category-list')

@login_required(login_url='/login')
def Category_Delete(request, Category_NO):
    data = Category_Model.objects.get(Category_NO=Category_NO)
    data.is_del = True
    data.save()
    return redirect('category-list')

@login_required(login_url='/login')
def Search_Category(request):
    title = request.GET['Searchcategory']
    data = Category_Model.objects.filter(
        Category_Name__icontains=title).filter(is_del__icontains=False)
    paginator = Paginator(data, 3)
    page_number = request.GET.get('page', 1)
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page = Paginator.page(0)
    return render(request, 'Category_list.html', {'dataFinal': dataFinal})
