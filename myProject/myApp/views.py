from django.shortcuts import render

def home(request):
    context={}
    return render(request, "myApp/home.html", context)

def dietplan(request):
    context={}
    return render(request, "myApp/dietplan.html", context)

def footballdrills(request):
    context={}
    return render(request, "myApp/footballdrills.html", context)

def strength(request):
    context={}
    return render(request, "myApp/strength.html", context)

def logfood(request):
    context={}
    return render(request, "myApp/logfood.html", context)

def recovery(request):
    context={}
    return render(request, "myApp/recovery.html", context)

def calender(request):
    context={}
    return render(request, "myApp/calender.html", context)

def wellbeing(request):
    context={}
    return render(request, "myApp/wellbeing.html", context)




