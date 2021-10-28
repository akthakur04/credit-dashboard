from django.shortcuts import render,redirect
from .models import *
from django.db.models import Sum, Avg
from django.http import JsonResponse
# Create your views here.
def login(request):
    if request.method=='POST':
        return redirect('home')
    else:
        return render(request, 'login.html')


def home(request):


    ctype1=datamodel.objects.filter(ChartType="New NPA Accounts")
    ctype2= datamodel.objects.filter(ChartType="NPA Accounts with recovery")
    ctype3 = datamodel.objects.filter(ChartType="New SMA Accounts")
    gnpa=list(ctype1.aggregate(Gross_Npa=Avg('AmountOutstanding')).values())
    recovery=list(ctype2.aggregate(Gross_Recovery=Avg('Recovery')).values())
    sma=list(ctype3.aggregate(Gross_Sma=Avg('AmountOutstanding')).values())
    sma2=list(ctype2.aggregate(Gross_Sma2=Avg('AmountOutstanding')).values())

    npadate=ctype1.values('Date').distinct()
    npardate=ctype1.values('Date').distinct()
    smaadate=ctype1.values('Date').distinct()

    qsests={
        "credits1": ctype1,
        "credits2": ctype2,
        "credits3": ctype3,
        "gnpa":gnpa,
        "recovery":recovery,
        "sma":sma,
        "sma2":sma2,
        "npadate":npadate,
        "npardate":npardate,
        "smadate":smaadate,

    }

    return render(request, 'home.html', qsests)


def population_chart(request):
    labels = []
    data = []

    queryset = datamodel.objects.values('CustomerName').annotate(country_population=Sum('AmountOutstanding')).order_by('CustomerId')
    for entry in queryset:
        labels.append(entry['CustomerName'])
        data.append(entry['country_population'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def newnpachar(request):
    labels = []
    data = []

    queryset = datamodel.objects.values('CustomerName').annotate(country_population=Sum('DaysOverdue')).order_by(
        'CustomerId')
    for entry in queryset:
        labels.append(entry['CustomerName'])
        data.append(entry['country_population'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })