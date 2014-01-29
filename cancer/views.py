#from django.shortcuts import render
# Create your views here.
from django.shortcuts import render_to_response
from django_tables2 import RequestConfig
from django.shortcuts import render
from django.template import RequestContext
from cancer.models import cancer
from cancer.models import smads
from cancer.models import targetedgene
from cancer.tables  import cancerTable
from cancer.tables  import smadTable
from cancer.tables  import genesTable


def cancersite(request):
	table = cancerTable(cancer.objects.all())
	RequestConfig(request, paginate=False).configure(table)
	return render(request, 'cancersite.html', {'cancertable': table})
    #main page based on request.


def smadsite(request):
	table = smadTable(smads.objects.all())
	RequestConfig(request, paginate=False).configure(table)
	return render(request, 'smadsite.html', {'smadtable': table})
  

def genesite(request):
	table = genesTable(targetedgene.objects.all())
	RequestConfig(request, paginate=False).configure(table)
	return render(request, 'genesite.html', {'genestable': table})


def mainpage(request):
    return render_to_response('mainpage.html') #main page based on request.