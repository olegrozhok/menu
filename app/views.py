from django.shortcuts import render


def home(request):
    return render(request, "base.html", locals())


def menu(request):
    return render(request, "main.html", locals())


def submenu1(request):
    return render(request, "submenu1.html", locals())


def submenu2(request):
    return render(request, "submenu2.html", locals())


def submenu3(request):
    return render(request, "submenu3.html", locals())
