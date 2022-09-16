import datetime
from django.core.paginator import EmptyPage, Paginator
from django.shortcuts import redirect, render
from Supplier.models import Supplier_models
from .forms import Voucher_forms
from .models import Payment_vouchers
from Tally_master.models import TallyModel


# Create your views here.
def list(request):
    data = Payment_vouchers.objects.filter(
        is_del=False).order_by('payment_date')
    paginator = Paginator(data, 20)
    page_number = request.GET.get('page', 1)
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page = Paginator.page(0)
    return render(request, 'Payment_list.html', {'dataFinal': dataFinal, })


def ledger_list(request):
    data = Payment_vouchers.objects.all().order_by('payment_date')
    paginator = Paginator(data, 3)
    page_number = request.GET.get('page', 1)
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page = Paginator.page(0)
    return render(request, 'ledger_list.html', {'dataFinal': dataFinal})


def PVoucher_forms(request):
    if request.method == 'GET':
        form = Voucher_forms()
        return render(request, 'payment_voucher.html', {'form': form})

    else:
        form = Voucher_forms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('voucher-list')


def voucher_edit_form(request, Payment_NO=0):
    if request.method == 'GET':
        if Payment_NO == 0:
            form = Voucher_forms()

        else:
            data1 = Payment_vouchers.objects.get(
                Payment_NO=Payment_NO)
            form = Voucher_forms(instance=data1)
        return render(request, 'voucher_edit.html', {'form': form})
    else:
        if Payment_NO == 0:
            form = Voucher_forms(request.POST)

        else:
            data1 = Payment_vouchers.objects.get(
                Payment_NO=Payment_NO)
            form = Voucher_forms(request.POST, instance=data1)

        if form.is_valid():
            form.save()
            return redirect('voucher-list')


def Voucher_Delete(request, Payment_NO):
    data = Payment_vouchers.objects.get(Payment_NO=Payment_NO)
    data.is_del = True
    data.save()
    return redirect('voucher-list')


def Search_voucher(request):
    title = request.GET['Searchvouchername']
    data = Payment_vouchers.objects.filter(
        Supplier_Name_id__Name__icontains=title).filter(is_del__icontains=False)
    print( data)
    paginator = Paginator(data, 3)
    page_number = request.GET.get('page', 1)
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page = Paginator.page(0)
    return render(request, 'Payment_list.html', {'dataFinal': dataFinal})


def Search_ledger(request):
    fromdate = request.POST.get('fromdate')
    todate = request.POST.get('todate')
    title = request.GET['Searchledgername']
    data = Payment_vouchers.objects.filter(Supplier_Name_id__Name__icontains=title).filter(
        date__range=["2011-01-01", datetime.datetime.today()]).filter(is_del__icontains=False)
    paginator = Paginator(data, 3)
    page_number = request.GET.get('page', 1)
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page = Paginator.page(0)
    return render(request, 'ledger_list.html', {'dataFinal': dataFinal})


def invoice(rqs):
    return render(rqs, 'invoice_print.html')

#def Voucher(rqs):
   # return render(rqs,'Voucher.html')

def get_print_data(request,Voucher_NO=None):
    data = Payment_vouchers.objects.all()if Voucher_NO is None else  Payment_vouchers.objects.filter( Payment_NO=Voucher_NO)
    print("data:",data)
    return render(request, "Voucher.html", {'data':data})
    