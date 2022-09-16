from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render

from .forms import City_Form
from .models import City_Model


# Create your views here.
@login_required(login_url='/login')
def list(request):
    data  =  City_Model.objects.filter(is_del=False).order_by('City_Code')
    paginator = Paginator(data,20)
    page_number = request.GET.get('page',1) 
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page=Paginator.page(0)
    return render (request,'City_list.html',{'dataFinal':dataFinal,})

@login_required(login_url='/login')    
def City_forms(request):
    error1 = None
    if request.method == 'GET':
        form = City_Form()
        return render(request,'city.html',{'form':form})
    else:
        form =City_Form(request.POST)
        if form.is_valid():
            error_count = 0
            city_name = form.cleaned_data['City_Name']
            if(len(city_name)<=2):
                error_count = error_count+1
                error1 = "City Name Must Be of Minimum 3 characters!"
                print("ran into an error")
                form.fields['City_Name'].widget.attrs['value'] = ''
                form.fields['City_Name'].widget.attrs['placeholder'] = 'Wrong value'
                form.fields['City_Name'].widget.attrs['style'] = 'border: 3px solid red'
            if(error_count!=0):    
                return render(request,'city.html',{'form':form,'error1':error1,})
            else:
                form.save()
                return redirect('city-list')
        return render(request,'city.html',{'form':form,'error1':error1,}) 

@login_required(login_url='/login')        
def City_edit_form(request,City_Code=0):
    if request.method == 'GET':
        if City_Code == 0:
            form = City_Form()

        else:
            data1 = City_Model.objects.get(City_Code=City_Code)
            form = City_Form(instance=data1)
        return render(request,'CITY_EDIT.html',{'form':form})
    else:
        if City_Code == 0:
            form =City_Form(request.POST)

        else:
            data1 = City_Model.objects.get(City_Code=City_Code)
            form = City_Form(request.POST,instance=data1)

        if form.is_valid():
            error_count = 0
            city_name = form.cleaned_data['City_Name']
            if(len(city_name)<=2):
                error_count = error_count+1
                error1 = "City Name Must Be of Minimum 3 characters!"
                print("ran into an error")
                form.fields['City_Name'].widget.attrs['value'] = ''
                form.fields['City_Name'].widget.attrs['placeholder'] = 'Wrong value'
                form.fields['City_Name'].widget.attrs['style'] = 'border: 3px solid red'
            if(error_count!=0):    
                return render(request,'city.html',{'form':form,'error1':error1,})
            else:
                form.save()
                return redirect('city-list')
        return render(request,'city.html',{'form':form,'error1':error1,}) 
        
@login_required(login_url='/login')        
def City_Delete(request,City_Code):
    data = City_Model.objects.get(City_Code=City_Code)
    data.is_del= True
    data.save()
    return redirect('city-list')

@login_required(login_url='/login')
def Search_City(request):
    title= request.GET['Searchcity']
    data = City_Model.objects.filter(City_Name__icontains=title).filter(is_del__icontains=False)
    paginator = Paginator(data,3)
    page_number = request.GET.get('page',1) 
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page=Paginator.page(0)
    return render(request,'City_list.html',{'dataFinal':dataFinal})
