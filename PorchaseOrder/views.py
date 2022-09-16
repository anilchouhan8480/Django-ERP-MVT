from django.contrib.auth.models import User
from django.db import transaction
from django.db.models import Max, Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from Item_Master.models import Item_Model
from Supplier.models import Supplier_models
from GST.models import Gst_Model
from .models import Puchase_oreder_meterial, PurchaseOrder
from django.urls import reverse
from State.models import State_Model
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from datetime import datetime

# Create your views here.

def Purchase_order(request):


    uObj = User.objects.get(username=request.user)

    uObj = Supplier_models.objects.all()
    IObj = Item_Model.objects.all()
    GObj = Gst_Model.objects.all()
    Sobj = State_Model.objects.all()

    if request.method == "POST":
        sc = request.POST['Supplier_code']
        arr_date = request.POST['delivery_date']
        location = request.POST['location']
        rm = request.POST['remark']

        p = PurchaseOrder(Supplier_Code_id=sc,Remark=rm, Expected_Arrival_date=arr_date,Location=location)
        result = p.save()
        print(result)



        data = PurchaseOrder.objects.latest('PO_No')
        print(data)

        field_name = 'PO_No'
        field_object = PurchaseOrder._meta.get_field(field_name)
        field_value = field_object.value_from_object(data)
        print("Field value : ", field_value)

        if field_value > 0:
            ic = request.POST['item_count']
            print(ic)

            def gst_calc(item_price,item_qty,gst_val):
                ttl_item_price = item_price*item_qty
                gs = ttl_item_price*gst_val
                gs_am = gs/100
                tota_cst =  ttl_item_price + gs_am
                return tota_cst

            for i in range(int(ic)):

                it_code = request.POST['item_code_'+str(i)]
                print(it_code)
                it_qty = request.POST['item_qty_'+str(i)]
                it_gst = request.POST['item_gst_'+str(i)]
                it_price = request.POST['item_price_'+str(i)]
                print("Gst Value",it_gst)

                it  = gst_calc(float(it_price),float(it_qty),float(it_gst))
                print(it)
                add = Puchase_oreder_meterial(Item_id_id=it_code, Item_quantity=it_qty,Gst_percent=it_gst,
                                             Item_basePrice=it_price, Total_Amount=it, Purchase_order_id=field_value)
                add.save()
                transaction.commit()
        else:
            pass

        return redirect('purchase-list')

    return render(request, "PorchaseOrder_Create.html", {"uObj":uObj, 'IObj': IObj,'GObj':GObj,'Sobj':Sobj,})


def purchase_list(request):
    data=Puchase_oreder_meterial.objects.filter(Purchase_order_id__is_del=False).order_by('PO_meterial_id')

    paginator = Paginator(data, 10)
    page_number = request.GET.get('page', 1)
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page = Paginator.page(0)

    return render(request, "puchaseOrder_List.html", {'dataFinal': dataFinal,'paginator':paginator})

    uObj = User.objects.get(username=request.user)
    pObj = PurchaseOrder.objects.get(PO_No=PO_No)
    IObj = Item_Model.objects.all()

    p = Puchase_oreder_meterial.objects.filter(PO_meterial_id=PO_No)

    if request.method == "POST":
        pom_id = request.POST.getlist('purchase_order_material_id[]')   
        it_code = request.POST.getlist('item_code[]')
        it_qty = request.POST.getlist('item_qty[]')
        it_price = request.POST.getlist('item_price[]')

        dt = datetime.now()

        i = 0
        while i < len(pom_id):
          print("print pom id",pom_id[i])
        
          Total = (float(it_qty[i]))*(float(it_price[i]))
          if pom_id[i] == '-1':
            print('insert')

            add = Puchase_oreder_meterial(Item_id_id=it_code[i], 
                Item_quantity=it_qty[i],
                Item_basePrice=it_price[i],
                Total_Amount=Total,
                Purchase_order_id=PO_No)

            add.save()
            return redirect('purchase-list')
            transaction.commit()
          else:
            print("update")

            pr = Puchase_oreder_meterial.objects.filter(PO_meterial_id=pom_id[i])
            pr.update(Item_id_id=it_code[i],
                Item_quantity=it_qty[i],
                Item_basePrice=it_price[i],
                Total_Amount=Total,Updated_At=dt)

          i += 1
        return redirect('purchase-list')
    return render(request,"purchaseOrder_Edit.html",{'pObj':pObj,'p':p,'IObj':IObj})

def Edit_po(request, PO_No):

    uObj = User.objects.get(username=request.user)
    # user = uObj

    pObj = PurchaseOrder.objects.get(PO_No=PO_No)
    IObj = Item_Model.objects.all()


    p = Puchase_oreder_meterial.objects.filter(Purchase_order_id=PO_No)

    # print("Value of P: ",p)
    if request.method == "POST":
        pom_id = request.POST.getlist('purchase_order_material_id[]')
           
        it_code = request.POST.getlist('item_code[]')
        it_qty = request.POST.getlist('item_qty[]')
        it_price = request.POST.getlist('item_price[]')

        dt = datetime.now()

        # now = datetime.now()

        # print(len(pom_id))

        i = 0
        while i < len(pom_id):
          # print("print pom id",pom_id[i])
        
          Total = (float(it_qty[i]))*(float(it_price[i]))
          if pom_id[i] == '-1':
            # print('insert')

            add = Puchase_oreder_meterial(Item_id_id=it_code[i], 
                Item_quantity=it_qty[i],
                Item_basePrice=it_price[i],
                Total_Amount=Total,
                Purchase_order_id=PO_No)

            add.save()
            return redirect('purchase-list')
            transaction.commit()
          else:
            print("update")

            pr = Puchase_oreder_meterial.objects.filter(PO_meterial_id=pom_id[i])
            pr.update(Item_id_id=it_code[i],
                Item_quantity=it_qty[i],
                Item_basePrice=it_price[i],
                Total_Amount=Total,Updated_At=dt)

          i += 1
        return redirect('purchase-list')
    return render(request, "purchaseOrder_Edit.html", {'pObj': pObj,'p':p,'IObj':IObj})

def Search_PO(request):
    title= request.POST['poo-number']
    title1=request.POST['supplier-codepo']
    title2=request.POST['supplier-namepo']
    title3=request.POST['item-codepo']
    title4=request.POST['item-namepo']
    data = Puchase_oreder_meterial.objects.filter(Purchase_order_id__PO_No__icontains=title).filter(Purchase_order_id__Supplier_Code_id__Supplier_Code__icontains=title1).filter(Purchase_order_id__Supplier_Code_id__Name__icontains=title2).filter(Item_id_id__Item_NO__icontains=title3).filter(Item_id_id__Item_Name__icontains=title4).filter(Purchase_order_id__is_del=False)
    paginator = Paginator(data, 3)
    page_number = request.GET.get('page', 1)
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page = Paginator.page(0)

    return render(request, "puchaseOrder_List.html", {'dataFinal': dataFinal,'paginator':paginator})


def PO_Delete(request,PO_No):
    data =PurchaseOrder.objects.get(PO_No=PO_No)
    data.is_del = True
    data.save()
    return redirect('purchase-list')

def get_print_data(request,PO_No=0):
    if PO_No==0:
        return render(request,"PurchaseOrder_Print2.html")
    else:
        data_pom=Puchase_oreder_meterial.objects.filter(Purchase_order_id=PO_No)
        print(data_pom)
        return render(request, "PurchaseOrder_Print2.html",{'data_pom':data_pom})
    




    #PrObj=Puchase_oreder_meterial.objects.all() if po_id is None else Puchase_oreder_meterial.objects.filter(Purchase_order_id=po_id).filter(Purchase_order_id__is_del=False)
   # print("PrObj:",PrObj)
   # return render(request, "PurchaseOrder_Print2.html", {'PrObj': PrObj})

