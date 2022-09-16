from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render

from .forms import Color_Forms
from .models import Color_Model


@login_required(login_url='/login')
def list(request):
    data  = Color_Model.objects.filter(is_del=False).order_by('Color_Code')
    paginator = Paginator(data,20)
    page_number = request.GET.get('page',1) 
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page=Paginator.page(0)
    return render (request,'Color_list.html',{'dataFinal':dataFinal,})

@login_required(login_url='/login')
def Color_forms(request):
    if request.method == 'GET':
        form = Color_Forms()
        return render(request,'color.html',{'form':form})
    else:
        form =Color_Forms(request.POST)
        if form.is_valid():
              error_count = 0
              color_Name = form.cleaned_data['Color_Name']
              if(len(color_Name)<=2):
                    error_count = error_count+1
                    error1 = " Color Name Must Be of Minimum 3 characters!"
                    print("ran into an error")
                    form.fields['Color_Name'].widget.attrs['value'] = ''
                    form.fields['Color_Name'].widget.attrs['placeholder'] = 'Wrong value'
                    form.fields['Color_Name'].widget.attrs['style'] = 'border: 3px solid red'
              if(error_count!=0):    
                    return render(request,'color.html',{'form':form,'error1':error1,})
              else:
                 form.save()
        return redirect('color-list')
    
@login_required(login_url='/login')    
def color_edit_form(request,Color_Code=0):
    if request.method == 'GET':
        if Color_Code == 0:
            form = Color_Forms()

        else:
            data1 = Color_Model.objects.get(Color_Code=Color_Code)
            form = Color_Forms(instance=data1)
        return render(request,'COLOR_EDIT.html',{'form':form})
    else:
        if Color_Code == 0:
            form = Color_Forms(request.POST)

        else:
            data1 = Color_Model.objects.get(Color_Code=Color_Code)
            form = Color_Forms(request.POST,instance=data1)

        if form.is_valid():
              error_count = 0
              color_Name = form.cleaned_data['Color_Name']
              if(len(color_Name)<=2):
                    error_count = error_count+1
                    error1 = " Color Name Must Be of Minimum 3 characters!"
                    print("ran into an error")
                    form.fields['Color_Name'].widget.attrs['value'] = ''
                    form.fields['Color_Name'].widget.attrs['placeholder'] = 'Wrong value'
                    form.fields['Color_Name'].widget.attrs['style'] = 'border: 3px solid red'
              if(error_count!=0):    
                    return render(request,'color.html',{'form':form,'error1':error1,})
              else:
                 form.save()
        return redirect('color-list')
        
@login_required(login_url='/login')        
def Color_Delete(request,Color_Code):
    data = Color_Model.objects.get(Color_Code=Color_Code)
    data.is_del = True
    data.save()
    return redirect('color-list')

@login_required(login_url='/login')
def Search_Color(request):
    title= request.GET['Searchcolorname']
    data = Color_Model.objects.filter(Color_Name__icontains=title).filter(is_del__icontains=False)
    paginator = Paginator(data,3)
    page_number = request.GET.get('page',1) 
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page=Paginator.page(0)
    return render(request,'Color_list.html',{'dataFinal':dataFinal})
