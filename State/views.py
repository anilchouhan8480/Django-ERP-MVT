from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render

from .forms import State_Form
from .models import State_Model


# Create your views here.
@login_required(login_url='/login')
def State_list(request):
    data = State_Model.objects.all()

    paginator = Paginator(data, 3)
    page_number = request.GET.get('page', 1)
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page = Paginator.page(0)
    
    return render(request, 'State_list.html', {'dataFinal': dataFinal})

@login_required(login_url='/login')
def state_Form(request):
    if request.method == 'GET':
        form = State_Form()
        return render(request, 'state.html', {'form': form})

    else:
        form = State_Form(request.POST)
        if form.is_valid():
            error_count = 0
            state_Name = form.cleaned_data['State_Name']
            if(len(state_Name) <= 2):
                error_count = error_count+1
                error1 = "State Name Must Be of Minimum 3 characters!"
                print("ran into an error")
                form.fields['State_Name'].widget.attrs['value'] = ''
                form.fields['State_Name'].widget.attrs['placeholder'] = 'Wrong value'
                form.fields['State_Name'].widget.attrs['style'] = 'border: 3px solid red'
            if(error_count != 0):
                return render(request, 'state.html', {'form': form, 'error1': error1, })
            else:
                form.save()
        return redirect('state-list')

@login_required(login_url='/login')
def State_edit_form(request, State_Code=0):
    if request.method == 'GET':
        if State_Code == 0:
            form = State_Form()

        else:
            data1 = State_Model.objects.get(State_Code=State_Code)
            form = State_Form(instance=data1)
        return render(request, 'STATE_EDIT.html', {'form': form})
    else:
        if State_Code == 0:
            form = State_Form(request.POST)

        else:
            data1 = State_Model.objects.get(State_Code=State_Code)
            form = State_Form(request.POST, instance=data1)

        if form.is_valid():
            error_count = 0
            state_Name = form.cleaned_data['State_Name']
            if(len(state_Name) <= 2):
                error_count = error_count+1
                error1 = "State Name Must Be of Minimum 3 characters!"
                print("ran into an error")
                form.fields['State_Name'].widget.attrs['value'] = ''
                form.fields['State_Name'].widget.attrs['placeholder'] = 'Wrong value'
                form.fields['State_Name'].widget.attrs['style'] = 'border: 3px solid red'
            if(error_count != 0):
                return render(request, 'STATE_EDIT.html', {'form': form, 'error1': error1, })
            else:
                form.save()
            return redirect('state-list')

@login_required(login_url='/login')
def State_Delete(request, State_Code):
    data = State_Model.objects.get(State_Code=State_Code)
    data.is_del = True
    data.save()
    return redirect('state-list')

@login_required(login_url='/login')
def search_State(request):
    title = request.GET['Searchstate']
    data = State_Model.objects.filter(
        State_Name__icontains=title).filter(is_del__icontains=False)
    paginator = Paginator(data, 3)
    page_number = request.GET.get('page', 1)
    try:
        dataFinal = paginator.get_page(page_number)
    except EmptyPage:
        page = Paginator.page(0)
    return render(request, 'State_list.html', {'dataFinal': dataFinal})
