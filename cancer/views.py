#from django.shortcuts import render
# Create your views here.
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from cancer.models import cancer
from cancer.models import smads
from cancer.models import targetedgene


def cancersite(request):
	#cancer_list = cancer.objects.all()
	#t = loader.get_template('cancer/index.html')
	#c = RequestContext({'cancer_list': cancer_list,})
    return render(request, 'cancersite.html', { 'cancer_list' : cancer.objects.all() }) #main page based on request.


def smadsite(request):
	#cancer_list = cancer.objects.all()
	#t = loader.get_template('cancer/index.html')
	#c = RequestContext({'cancer_list': cancer_list,})
    return render(request, 'smadsite.html', { 'smads_list' : smads.objects.all()  }) #main page based on request.


def genesite(request):
	#cancer_list = cancer.objects.all()
	#t = loader.get_template('cancer/index.html')
	#c = RequestContext({'cancer_list': cancer_list,})
    return render(request, 'genesite.html', { 'targetedgene_list' : targetedgene.objects.all() }) #main page based on request.


def mainpage(request):
    return render_to_response('mainpage.html') #main page based on request.