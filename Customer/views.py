from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, Paginator
from django.db import transaction
from django.shortcuts import redirect, render
from State.models import State_Model

from .forms import Customer_Forms
from .models import Customer_models


@login_required(login_url='/login')
# Create your views here.
def Customer_list(request):
    uObj = State_Model.objects.all()
    data = Customer_models.objects.filter(is_del=False).order_by('Customer_Code')
    paginator = Paginator(data,20)
    page_number = request.GET.get('page',1) 
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page=Paginator.page(0)
    
    return render (request,'Customer_List.html',
                   {'dataFinal':dataFinal,
                    'paginator':paginator,
                    'uObj':uObj
                    })
@login_required(login_url='/login')                    
def Customer_add_form(request):
    uObj = State_Model.objects.all()
    error1=error2=error3=error4=error5=error6=error7=None
    if request.method=='GET':
        form= Customer_Forms()
        return render(request,'Customer_Create.html',{'form':form,'uObj':uObj})
    else:
        form= Customer_Forms(request.POST,request.FILES)
        if form.is_valid():
           error_count = 0
           name = form.cleaned_data['Name']
           mobile = form.cleaned_data['Mobile_NO']
           bname= form.cleaned_data['Billing_Name']
           gst = form.cleaned_data['GSTIN']
           pcode= form.cleaned_data['postalcode']
           sname= form.cleaned_data['Name_shipping']
           spcode= form.cleaned_data['postalcode_ship']
           if(len(name)<=2):
                error_count = error_count+1
                error1 = "Supplier Name Must Contain  Minimum 3 characters!"
                form.fields['Name'].widget.attrs['value'] = ''
                form.fields['Name'].widget.attrs['placeholder'] = 'Wrong value'
                form.fields['Name'].widget.attrs['style'] = 'border: 3px solid red'   
           if(len(str(mobile))!=10):
                error_count = error_count+1
                error2 = "Mobile Number Must Be 10 Digits Long!"
                form.fields['Mobile_NO'].widget.attrs['value'] = ''
                form.fields['Mobile_NO'].widget.attrs['style'] = 'border: 3px solid red'
                
           if(len(bname)<=2):
                error_count = error_count+1
                error3 = "Billing Name Must Contain  Minimum 3 characters!"
                form.fields['Billing_Name'].widget.attrs['value'] = ''
                form.fields['Billing_Name'].widget.attrs['placeholder'] = 'Wrong value'
                form.fields['Billing_Name'].widget.attrs['style'] = 'border: 3px solid red'
           if(len(gst)!=15):
                error_count = error_count+1
                error4 = "GST Number Must Contain 15 Characters! "
                form.fields['GSTIN'].widget.attrs['value'] = ''
                form.fields['GSTIN'].widget.attrs['style'] = 'border: 3px solid red'
           if(len(str(pcode))!=6):
                error_count = error_count+1
                error5 = "Postal Code Requires 6  Digits!"
                form.fields['postalcode'].widget.attrs['value'] = ''
                form.fields['postalcode'].widget.attrs['style'] = 'border: 3px solid red'
           if(len(sname)<=2):
                error_count = error_count+1
                error6 = "Name of Shipping  Must Contain  Minimum 3 characters!"
                form.fields['Name_shipping'].widget.attrs['value'] = ''
                form.fields['Name_shipping'].widget.attrs['placeholder'] = 'Wrong value'
                form.fields['Name_shipping'].widget.attrs['style'] = 'border: 3px solid red'
           if(len(str(spcode))!=6):
                error_count = error_count+1
                error7 = "Postal  Code of Shipping Requires 6  Digits!"
                form.fields['postalcode_ship'].widget.attrs['value'] = ''
                form.fields['postalcode_ship'].widget.attrs['style'] = 'border: 3px solid red'
           if(error_count!=0):  
                return render(request,'Customer_Create.html',{'form':form,'uObj':uObj,'error1':error1,
                                                   'error2':error2,'error3':error3,'error4':error4,'error5':error5,'error6':error6,
                                                   'error7':error7})
           else:
                form.save()
                return redirect('customer-list')
        return render(request,'Customer_Create.html',{'form':form,'uObj':uObj,'error1':error1,
                                    'error2':error2,'error3':error3,'error4':error4,'error5':error5,'error6':error6,'error7':error7})
@login_required(login_url='/login')        
def edit_cs_form(request,Customer_Code=0):
    error1=error2=error3=error4=error5=error6=error7=None
    if request.method == 'GET':
        if Customer_Code == 0:
            form = Customer_Forms()

        else:
            data = Customer_models.objects.get(Customer_Code=Customer_Code)
            form = Customer_Forms(instance=data)
            

        return render(request,'Customer_Edit.html',{'form':form,})
    else:
        if Customer_Code == 0:
            form = Customer_Forms(request.POST)

        else:
            data = Customer_models.objects.get(Customer_Code=Customer_Code)
            form = Customer_Forms(request.POST,instance=data)
            
        if form.is_valid():
            error_count = 0
            name = form.cleaned_data['Name']
            mobile = form.cleaned_data['Mobile_NO']
            bname= form.cleaned_data['Billing_Name']
            gst = form.cleaned_data['GSTIN']
            pcode= form.cleaned_data['postalcode']
            sname= form.cleaned_data['Name_shipping']
            spcode= form.cleaned_data['postalcode_ship']
            if(len(name)<=2):
                error_count = error_count+1
                error1 = "Supplier Name Must Contain  Minimum 3 characters!"
                form.fields['Name'].widget.attrs['value'] = ''
                form.fields['Name'].widget.attrs['placeholder'] = 'Wrong value'
                form.fields['Name'].widget.attrs['style'] = 'border: 3px solid red'   
            if(len(str(mobile))!=10):
                error_count = error_count+1
                error2 = "Mobile Number Must Be 10 Digits Long!"
                form.fields['Mobile_NO'].widget.attrs['value'] = ''
                form.fields['Mobile_NO'].widget.attrs['style'] = 'border: 3px solid red'
                
            if(len(bname)<=2):
                error_count = error_count+1
                error3 = "Billing Name Must Contain  Minimum 3 characters!"
                form.fields['Billing_Name'].widget.attrs['value'] = ''
                form.fields['Billing_Name'].widget.attrs['placeholder'] = 'Wrong value'
                form.fields['Billing_Name'].widget.attrs['style'] = 'border: 3px solid red'
            if(len(gst)!=15):
                error_count = error_count+1
                error4 = "GST Number Must Contain 15 Characters! "
                form.fields['GSTIN'].widget.attrs['value'] = ''
                form.fields['GSTIN'].widget.attrs['style'] = 'border: 3px solid red'
            if(len(str(pcode))!=6):
                error_count = error_count+1
                error5 = "Postal Code Requires 6  Digits!"
                form.fields['postalcode'].widget.attrs['value'] = ''
                form.fields['postalcode'].widget.attrs['style'] = 'border: 3px solid red'
            if(len(sname)<=2):
                error_count = error_count+1
                error6 = "Name of Shipping  Must Contain  Minimum 3 characters!"
                form.fields['Name_shipping'].widget.attrs['value'] = ''
                form.fields['Name_shipping'].widget.attrs['placeholder'] = 'Wrong value'
                form.fields['Name_shipping'].widget.attrs['style'] = 'border: 3px solid red'
            if(len(str(spcode))!=6):
                error_count = error_count+1
                error7 = "Postal  Code of Shipping Requires 6  Digits!"
                form.fields['postalcode_ship'].widget.attrs['value'] = ''
                form.fields['postalcode_ship'].widget.attrs['style'] = 'border: 3px solid red'
            if(error_count!=0):  
                return render(request,'Customer_Create.html',{'form':form,'error1':error1,
                                                   'error2':error2,'error3':error3,'error4':error4,'error5':error5,'error6':error6,
                                                   'error7':error7})
            else:
                form.save()
            return redirect('customer-list')
       
@login_required(login_url='/login')            
def Customer_Delete(request,Customer_Code):
    data = Customer_models.objects.get(Customer_Code=Customer_Code)
    data.is_del = True
    data.save()
    return redirect('customer-list')
@login_required(login_url='/login')
def Search_Customer(request):
    title= request.POST['Searchname']
    title1=request.POST['SearchCode']
    title2=request.POST['SearchGST']
    data = Customer_models.objects.filter(Name__icontains=title).filter(Customer_Code__icontains=title1).filter(GSTIN__icontains=title2).filter(is_del__icontains=False)
    paginator = Paginator(data,3)
    page_number = request.GET.get('page',1) 
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page=Paginator.page(0)
    return render(request,'Customer_List.html',{'dataFinal':dataFinal})
    
    
