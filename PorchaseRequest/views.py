from django.contrib.auth.models import User
from django.db import transaction
from django.db.models import Max, Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from Item_Master.models import Item_Model
from Supplier.models import Supplier_models
from GST.models import Gst_Model
from .models import Puchase_request_meterial, PurchaseRequest
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from State.models import State_Model
from datetime import datetime

def pr_list(request):

	data=Puchase_request_meterial.objects.filter(is_del=False).order_by('PR_meterial_id')

	paginator = Paginator(data, 3)
	page_number = request.GET.get('page', 1)
	try:
		dataFinal = paginator.get_page(page_number)
	except EmptyPage:
		page = Paginator.page(0)

	return render(request, "PurchaseRequest_List.html",{'dataFinal': dataFinal,'paginator':paginator})

def Edit_pr(request,PR_No):
    pObj = PurchaseRequest.objects.get(PR_No=PR_No)
    IObj = Item_Model.objects.all()

    p = Puchase_request_meterial.objects.filter(Purchase_request_id=PR_No)
    

    print("Value of P: ",p)
    if request.method == "POST":
        pom_id = request.POST.getlist('Puchase_request_meterial_id[]')           
        it_code = request.POST.getlist('item_code[]')
        it_qty = request.POST.getlist('item_qty[]')
        it_price = request.POST.getlist('item_price[]')

        dt = datetime.now()

        print(len(pom_id))

        i = 0
        while i < len(pom_id):
          print("print pom id",pom_id[i])
         

          Total = (float(it_qty[i]))*(float(it_price[i]))
          if pom_id[i] == '-1':
            print('insert')

            add = Puchase_request_meterial(Item_id_id=it_code[i], 
                Item_quantity=it_qty[i],
                Item_basePrice=it_price[i],
                Total_Amount=Total,
                Purchase_request_id=PR_No)

            add.save()
            return redirect('pr-list')
            transaction.commit()


          else:
            print("update")
            pr = Puchase_request_meterial.objects.filter(PR_meterial_id=pom_id[i])
            pr.update(Item_id_id=it_code[i],
                Item_quantity=it_qty[i],
                Item_basePrice=it_price[i],
                Total_Amount=Total,Updated_At=dt)

          i += 1
        return redirect('pr-list')
    return render(request, "PurchaseRequest_Edit.html", {'pObj': pObj,'p':p,'IObj':IObj})


def Purchase_request(request):
	
	uObj = Supplier_models.objects.all()
	IObj = Item_Model.objects.all()
	GObj = Gst_Model.objects.all()
	Sobj = State_Model.objects.all()

	if request.method == "POST":
		sc = request.POST['Supplier_code']
		d = request.POST['desc']
		r = request.POST['req']
		ic = request.POST['item_co']
		arr_date = request.POST['arrival_date']
		location = request.POST['location']
		rm = request.POST['remark']

		p = PurchaseRequest(Supplier_Code_id=sc, Description=d,Requistioner=r,Item_Count=ic,Remark=rm,Expected_Arrival_date=arr_date,Location=location)
		p.save()

		data = PurchaseRequest.objects.latest('PR_No')
		#print(data)
		field_name = 'PR_No'
		field_object = PurchaseRequest._meta.get_field(field_name)
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
				add = Puchase_request_meterial(Item_id_id=it_code, Item_quantity=it_qty,Gst_percent=it_gst,
                                              Item_basePrice=it_price, Total_Amount=it, Purchase_request_id=field_value)
				add.save()
				transaction.commit()
			else:
				pass
		return redirect('pr-list')
	return render(request, "PurchaseRequest_Create.html", {"uObj": uObj, 'IObj': IObj,'GObj':GObj,'Sobj':Sobj})
def Search_PR(request):
    title= request.POST['pr-number']
    title1=request.POST['supplier-codepr']
    title2=request.POST['supplier-namepr']
    title3=request.POST['item-codepr']
    title4=request.POST['item-namepr']
    data = Puchase_request_meterial.objects.filter(Purchase_request_id__PR_No__icontains=title).filter(Purchase_request_id__Supplier_Code_id__Supplier_Code__icontains=title1).filter(Purchase_request_id__Supplier_Code_id__Name__icontains=title2).filter(Item_id_id__Item_NO__icontains=title3).filter(Item_id_id__Item_Name__icontains=title4).filter(is_del__icontains=False)
    return render(request,'PurchaseRequest_List.html',{'data':data})

def PR_Delete(request,PR_meterial_id):
    data =Puchase_request_meterial.objects.get(PR_meterial_id=PR_meterial_id)
    data.is_del = True
    data.save()
    return redirect('pr-list')