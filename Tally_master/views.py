from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render

from .forms import Tally_Forms
from .models import TallyModel


@login_required(login_url='/login')
def list(request):
    data  = TallyModel.objects.filter(is_del=False).order_by('Tally_NO')
    paginator = Paginator(data,20)
    page_number = request.GET.get('page',1) 
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page=Paginator.page(0)
    return render (request,'Tally_list.html',{'dataFinal':dataFinal,})

@login_required(login_url='/login')
def Tally_forms(request):
    if request.method == 'GET':
        form = Tally_Forms()
        return render(request,'Tally.html',{'form':form})
    else:
        form =Tally_Forms(request.POST)
        if form.is_valid():
              error_count = 0
              Data_Name = form.cleaned_data['Data_Name']
              if(len(Data_Name)<=2):
                    error_count = error_count+1
                    error1 = " Tally Name Must Be of Minimum 3 characters!"
                    print("ran into an error")
                    form.fields['Data_Name'].widget.attrs['value'] = ''
                    form.fields['Data_Name'].widget.attrs['placeholder'] = 'Wrong value'
                    form.fields['Data_Name'].widget.attrs['style'] = 'border: 3px solid red'
              if(error_count!=0):    
                    return render(request,'Tally.html',{'form':form,'error1':error1,})
              else:
                 form.save()
        return redirect('Tally-list')
    
@login_required(login_url='/login')    
def Tally_edit_form(request,Tally_NO=0):
    if request.method == 'GET':
        if Tally_NO == 0:
            form = Tally_Forms()

        else:
            data1 = TallyModel.objects.get(Tally_NO=Tally_NO)
            form = Tally_Forms(instance=data1)
        return render(request,'Tally_EDIT.html',{'form':form})
    else:
        if Tally_NO == 0:
            form = Tally_Forms(request.POST)

        else:
            data1 = TallyModel.objects.get(Tally_NO=Tally_NO)
            form = Tally_Forms(request.POST,instance=data1)

        if form.is_valid():
              error_count = 0
              Data_Name = form.cleaned_data['Data_Name']
              if(len(Data_Name)<=2):
                    error_count = error_count+1
                    error1 = " Tally Name Must Be of Minimum 3 characters!"
                    print("ran into an error")
                    form.fields['Data_Name'].widget.attrs['value'] = ''
                    form.fields['Data_Name'].widget.attrs['placeholder'] = 'Wrong value'
                    form.fields['Data_Name'].widget.attrs['style'] = 'border: 3px solid red'
              if(error_count!=0):    
                    return render(request,'Tally.html',{'form':form,'error1':error1,})
              else:
                 form.save()
        return redirect('Tally-list')
        
@login_required(login_url='/login')        
def Tally_Delete(request,Tally_NO):
    data = TallyModel.objects.get(Tally_NO=Tally_NO)
    data.is_del = True
    data.save()
    return redirect('Tally-list')

@login_required(login_url='/login')
def Search_Tally(request):
    title= request.GET['SearchTallyname']
    data = TallyModel.objects.filter(Data_Name__icontains=title).filter(is_del__icontains=False)
    paginator = Paginator(data,3)
    page_number = request.GET.get('page',1) 
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page=Paginator.page(0)
    return render(request,'Tally_list.html',{'dataFinal':dataFinal})
