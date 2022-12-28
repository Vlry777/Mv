from django.shortcuts import render
from django.http import HttpResponse
from Familia.models import Family

def create_family_memebers(request):
    create_familiar= Family.objects.create(name = 'Delfina', surname = 'Barbano',
     age = 8, dni= 52458700, alive= True)
    print(create_familiar)
    return HttpResponse('Familiar añadido')

def list_family_members(request):
    all_family_members = Family.objects.all()
    context = {
        'family': all_family_members
    }
    return render(request,'list_families.html', context=context)

