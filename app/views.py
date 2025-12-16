from django.shortcuts import render,redirect
from django.http import HttpResponse;
from django.contrib import messages
from .models import Note

# Create your views here.
def indexView(req):
    notes=Note.objects.all()
    return render(req,"index.html",context={'notes':notes})

def aboutMe(req):
    return render(req,"about.html")

def saveDataView(req):
    print(req.POST)
    print("helllo from post")

    title=req.POST.get("title","")
    description=req.POST.get("description","")

    if not title or not description:
        #show the error
        messages.error(req,"Fill all the details")
        return redirect("/")
    
    note=Note(title=title,description=description) 
    note.save()
# title and description has come from the model. And created_At and isPublic has come by default.


     # data Saved
    messages.success(req,"Details saved")
    return redirect("/")

 # Delete view with unique primary keys
def deleteView(req,id):
    note=Note.objects.get(id=id) 
    note.delete()
    messages.success(req,"Note Deleted successfully..")
    return redirect("/") 

def updateViewPage(req,id):
    note=Note.objects.get(id=id)
    if req.method== "POST":
        title=req.POST.get("title","")
        description=req.POST.get("description","")
        published=req.POST.get("published","")
        published=True if published=='on' else False
        print(published)

        if not title or not description:
             messages.error(req,"Fill all details")

        note.title=title
        note.description=description
        note.isPublish=published
        note.save()   
        messages.success(req,"Details updated successfully")
            
  
    return render(req,"edit-page.html",context={
        "note":note
    })
     
 


 