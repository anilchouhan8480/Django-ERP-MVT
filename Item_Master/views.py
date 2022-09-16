from Color.models import Color_Model
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render
from GST.models import Gst_Model
from ITEM_Category.models import Category_Model

from .forms import Item_form
from .models import Item_Model


# Create your views here.
@login_required(login_url='/login')
def item_list(request):
    Category_data=Category_Model.objects.all()
    Gst_data=Gst_Model.objects.all()
    Color_data=Color_Model.objects.all()
    data = Item_Model.objects.filter(is_del=False).order_by('Item_NO')
    paginator = Paginator(data,20)
    page_number = request.GET.get('page',1) 
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page=Paginator.page(0)
    
    return render (request,'Item_List.html',
                   {'dataFinal':dataFinal,
                    'paginator':paginator,
                    'Category_data':Category_data,
                    'Gst_data':Gst_data,
                    'Color_data':Color_data
                    })
@login_required(login_url='/login')                    
def item_add_form(request):
    Category_data=Category_Model.objects.all()
    Gst_data=Category_Model.objects.all()
    if request.method=='GET':
        form= Item_form()
        return render(request,'Item_Create.html',{'form':form})
    else:
        form= Item_form(request.POST,request.FILES)
        if form.is_valid():
            error_count = 0
            item_name = form.cleaned_data['Item_Name']
            if(len(item_name)<=2):
                error_count = error_count+1
                error1 = "Item Name Must Be of Minimum 3 characters!"
                print("ran into an error")
                form.fields['Item_Name'].widget.attrs['value'] = ''
                form.fields['Item_Name'].widget.attrs['placeholder'] = 'Wrong value'
                form.fields['Item_Name'].widget.attrs['style'] = 'border: 3px solid red'
            if(error_count!=0):    
                return render(request,'Item_Create.html',{'form':form,'error1':error1,})
            else:
                form.save()
                return redirect('item-list')
        return render(request,'Item_Create.html',{'form':form,'error1':error1,}) 
@login_required(login_url='/login')          
def edit_form(request,Item_NO=0):
    print("hlo")
    if request.method == 'GET':
        if Item_NO == 0:
            form = Item_form()

        else:
            data = Item_Model.objects.get(Item_NO=Item_NO)
            form = Item_form(instance=data)

        return render(request,'Item_Edit.html',{'form':form,})
    else:
        if Item_NO == 0:
            form = Item_form(request.POST)

        else:
            data = Item_Model.objects.get(Item_NO=Item_NO)
            form = Item_form(request.POST,instance=data)

        if form.is_valid():
            error_count = 0
            item_name = form.cleaned_data['Item_Name']
            if(len(item_name)<=2):
                error_count = error_count+1
                error1 = "Item Name Must Be of Minimum 3 characters!"
                print("ran into an error")
                form.fields['Item_Name'].widget.attrs['value'] = ''
                form.fields['Item_Name'].widget.attrs['placeholder'] = 'Wrong value'
                form.fields['Item_Name'].widget.attrs['style'] = 'border: 3px solid red'
            if(error_count!=0):    
                return render(request,'Item_Create.html',{'form':form,'error1':error1,})
            else:
                form.save()
            return redirect('item-list')
@login_required(login_url='/login')        
def Item_Delete(request,Item_NO):
    data = Item_Model.objects.get(Item_NO=Item_NO)
    data.is_del = True
    data.save()
    return redirect('item-list')
@login_required(login_url='/login')
def Search_Item(request):
    title= request.GET['Searchname']
    title2= request.GET['Searchitemno']
    title3= request.GET['Searchhsn']
    data = Item_Model.objects.filter(Item_Name__icontains=title).filter(Item_NO__icontains=title2).filter(Item_Category_id__HSN_Code__icontains=title3).filter(is_del__icontains=False)
    paginator = Paginator(data,3)
    page_number = request.GET.get('page',1) 
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page=Paginator.page(0)
    return render(request,'Item_List.html',{'dataFinal':dataFinal})
