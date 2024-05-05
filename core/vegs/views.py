from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse

# Create your views here.
def receipes(request):
    if request.method=="POST":
     data=request.POST
     receipe_image = request.FILES.get('receipe_image')
     recepie_name = data.get('recepie_name')
     text = data.get('text')

     Recepie.objects.create(
         receipe_image = receipe_image,
         recepie_name = recepie_name,
         text = text,
     )

     return redirect('/receipes')
    
    queryset= Recepie.objects.all()
    context = {'receipes': queryset}    
    return render(request, 'receipes.html',context)

def delete_receipe(request,id):
   queryset = Recepie.objects.get(id= id)
   queryset.delete()
   return redirect('/receipes')
  