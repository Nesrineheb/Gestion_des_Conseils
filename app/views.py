# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from django.shortcuts import redirect, render
from .models import Document
from .forms import DocumentForm
from .models import Expert
from .models import Jury

@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'page-blank.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

def my_view(request):
    print(f"Great! You're using Python 3.6+. If you fail here, use the right version.")
    message = 'Upload as many files as you want!'
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return redirect('my-view')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'ui-collapse.html', context)
def TousLesExpert(request):
    if request.method == 'POST':
        e =Expert()
        e.Nom = request.POST.get('Nom')
        e.Prenom = request.POST.get('Prenom')
        e.Domaine = request.POST.get('Domaine')
        e.Grade= request.POST.get('Grade')
        e.Annee_expertise= request.POST.get('AnExp')
        e.Etablissement =request.POST.get('Etablissement')
        e.Num_teleph =request.POST.get('Num')
        e.Email=request.POST.get('Email')
        e.Matricule =request.POST.get('Matricule')
        e.save()
    

    listExperts = Expert.objects.all()
    listJurys = Jury.objects.all()
    return render(request, "ui-tables.html", {"expert": listExperts,"Jury": listJurys})

def delete(request,id):
    Expert.objects.filter(id=id).delete()
    listExperts = Expert.objects.all()
    return render(request, "ui-tables.html", {"expert": listExperts})



def TousLesTheses(request):
    if request.method == 'POST':
        e=Sujet()
        e.Sujet= request.POST.get('Sujet')
        e.Avis = request.POST.get('Avis')
        e.MotsCles = request.POST.get('MotsCles')
        e.save()
    listSujets= Sujet.objects.all()
  
    return render(request, "historiquedecision.html", {"these_decision": listSujets})
