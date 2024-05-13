from django.shortcuts import render,redirect

from .models import *
# Create your views here.
def receipes(request):
    if request.method =="POST":

        data =request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get("receipe_name")
        text = data.get("text")

        Receipe.objects.create(
             receipe_image =  receipe_image,
             receipe_name = receipe_name,
             text = text,

        )

       
        
        return redirect('/receipes')
    
    queryset = Receipe.objects.all()
    context = {'receipes': queryset}

   
        
        
    
    return render(request, 'receipes.html',context)

def login(request):
    return render(request,'login.html')


def update_receipe(request,id):
    queryset = Receipe.objects.get(id =id)
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get("receipe_name")
        text = data.get("text")

        queryset.receipe_name = receipe_name
        queryset.text = text
        if receipe_image:
            queryset.receipe_image = receipe_image
        queryset.save()
        return redirect('/receipes')

    context = {'receipe':queryset}
    return render(request, 'update_receipes.html', context)


def delete_receipe(request, id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/receipes')


