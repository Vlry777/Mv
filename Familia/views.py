from django.shortcuts import render
from django.http import HttpResponse
from Familia.models import Family

def create_family_memebers(request):
    create_familiar= Family.objects.create(name = 'Mara', surname = 'Hernandez',
     age = 14, dni= 49027020, alive= True)
    print(create_familiar)
    return HttpResponse('Familiar añadido')

def list_family_members(request):
    all_family_members = Family.objects.all()
    context = {
        'family': all_family_members
    }
    return render(request,'list_families.html', context=context)


