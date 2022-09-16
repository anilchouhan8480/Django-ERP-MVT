from django.core.paginator import EmptyPage, Paginator
from django.shortcuts import redirect, render
from State.models import State_Model
from .forms import Supplier_Forms
from .models import Supplier_models
from PorchaseOrder.models import PurchaseOrder,Puchase_oreder_meterial
from Purchase_Voucher.models import Payment_vouchers
# Create your views here.
def Supplier_list(request):
    uObj = State_Model.objects.all()
    data = Supplier_models.objects.filter(is_del=False).order_by('Supplier_Code')
    
    paginator = Paginator(data,3)
    page_number = request.GET.get('page',1) 
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page=Paginator.page(1)
    return render (request,'Supplier_List.html',
                   {'dataFinal':dataFinal,
                    'paginator':paginator,
                    'uObj':uObj})
def Supplier_add_form(request):
    uObj = State_Model.objects.all()
    error1=error2=error3=error4=error5=None
    if request.method=='GET':
        form= Supplier_Forms()
        return render(request,'Supplier_Create.html',{'form':form})
    else:
        form= Supplier_Forms(request.POST,request.FILES)
        if form.is_valid():
            error_count = 0
            name = form.cleaned_data['Name']
            mobile = form.cleaned_data['Mobile_NO']
            bname= form.cleaned_data['Billing_Name']
            gst = form.cleaned_data['GSTIN']
            pcode= form.cleaned_data['postalcode']
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
                
            if(error_count!=0):  
                return render(request,'Supplier_Create.html',{'form':form,'uObj':uObj,'error1':error1,
                                                   'error2':error2,'error3':error3,'error4':error4,'error5':error5})
            else:
                form.save()
                return redirect('supplier-list')
        return render(request,'Supplier_Create.html',{'form':form,'uObj':uObj,'error1':error1,
                                    'error2':error2,'error3':error3,'error4':error4,'error5':error5})
        
def edit_sup_form(request,Supplier_Code=0):
    error1=error2=error3=error4=error5=None
    if request.method == 'GET':
        if Supplier_Code == 0:
            form = Supplier_Forms()
        else:
            data = Supplier_models.objects.get(Supplier_Code=Supplier_Code)
            form = Supplier_Forms(instance=data)

        return render(request,'Supplier_Edit.html',{'form':form})
    else:
        if Supplier_Code == 0:
            form = Supplier_Forms(request.POST)

        else:
            data = Supplier_models.objects.get(Supplier_Code=Supplier_Code)
            form = Supplier_Forms(request.POST,instance=data)

        if form.is_valid():
            error_count = 0
            name = form.cleaned_data['Name']
            mobile = form.cleaned_data['Mobile_NO']
            bname= form.cleaned_data['Billing_Name']
            gst = form.cleaned_data['GSTIN']
            pcode= form.cleaned_data['postalcode']
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
                
            if(error_count!=0):  
                return render(request,'Supplier_Create.html',{'form':form,'error1':error1,
               'error2':error2,'error3':error3,'error4':error4,'error5':error5})
            else:
                form.save()
            return redirect('supplier-list')
    
def Supplier_Delete(request,Supplier_Code):
    data = Supplier_models.objects.get(Supplier_Code=Supplier_Code)
    data.is_del = True
    data.save()
    return redirect('supplier-list')

def Search_Supplier(request):
    title= request.POST['Searchname']
    title1=request.POST['SearchCode']
    title2=request.POST['SearchGST']
    title3=request.POST['Searchcity']
    title4=request.POST['Searchproduct']
    data = Supplier_models.objects.filter(Name__icontains=title).filter(Supplier_Code__icontains=title1).filter(GSTIN__icontains=title2).filter(City__icontains=title3).filter(suppliers_product__icontains=title4).filter(is_del__icontains=False)
    paginator = Paginator(data,3)
    page_number = request.GET.get('page',1) 
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page=Paginator.page(0)
    return render(request,'Supplier_List.html',{'dataFinal':dataFinal})

def details(request,Supplier_Code=0):
    if Supplier_Code==0:
       return  render(request, 'Supplier_Detail.html')
    else:
        data_supplier=Supplier_models.objects.get(Supplier_Code=Supplier_Code)
        data = Puchase_oreder_meterial.objects.filter(Purchase_order_id__Supplier_Code_id__Supplier_Code=Supplier_Code)
        print(data)
        data_ledger=Payment_vouchers.objects.filter(Supplier_Name_id__Supplier_Code=Supplier_Code).filter(is_del__icontains=False)
        print(data_ledger)
        return  render(request, 'Supplier_Detail.html',{'data':data,'data_ledger':data_ledger,'data_supplier':data_supplier})	            
