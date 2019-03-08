from django.shortcuts import render
from .models import Banks,Branches
from .forms import IfscForm, BranchForm

def index(request):
    return render(request, 'Bank/index.html')


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form1 = IfscForm(request.POST)
        # check whether it's valid:
        if form1.is_valid():
            obj = Branches.objects.all().filter(ifsc=form1.cleaned_data['Bank_ifsc'])
            my_dic = {'banks': obj}
            return render(request, 'Bank/results.html', my_dic)
    else:
        form1 = IfscForm()

    return render(request, 'Bank/form_page.html', {'form1': form1})




def branch_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:

        form2 = BranchForm(request.POST)
        # check whether it's valid:
        if  form2.is_valid():
            # a = Bank.objects.all().filter(city=form2.cleaned_data['Bank_city'])
            # my_dic = {'e': a }
            obj = Branches.objects.all().filter(city=form2.cleaned_data['Bank_city'])
            my_dic = {'bank': obj }
            return render(request, 'Bank/results1.html', my_dic)
    else:

        form2 = BranchForm()
    return render(request, 'Bank/form_page.html', {'form2': form2})
