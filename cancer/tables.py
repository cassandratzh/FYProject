import django_tables2 as tables
from cancer.models import cancer
from cancer.models import smads
from cancer.models import targetedgene

class cancerTable(tables.Table):
  cancertype = tables.Column(verbose_name= 'Types of Cancer' )
  subtype = tables.Column(verbose_name= 'Subtypes' )
  cellline = tables.Column(verbose_name= 'Cell Lines' )

  class Meta:
    model = cancer
    attrs = {'class': 'paleblue', 'width':'100%'}
    fields = ('cancertype', 'subtype', 'cellline') # fields to display


class smadTable(tables.Table):
  cellline = tables.Column(verbose_name= 'Cell Lines')
  smadtype = tables.Column(verbose_name= 'Types of Smad' )
  targetedgenes = tables.Column(verbose_name= 'Tageted Genes' )
  #targetedgenes = tables.TemplateColumn('<a href="/targetedgenes/">{{targetedgenes}}</a>')

  class Meta:
    model = smads
    attrs = {'class': 'paleblue', 'width':'90%'}
    fields = ('cellline', 'smadtype', 'targetedgenes') # fields to display


class genesTable(tables.Table):
  targetedgenes = tables.Column(verbose_name= 'Gene Symbol')
  fullnamegene = tables.Column(verbose_name= 'Gene Name' )
  entrezgene = tables.Column(verbose_name= 'Entrez' )
  refseqgene = tables.Column(verbose_name= 'RefSeq ')
  chromlocation = tables.Column(verbose_name= 'Chromosome No.' )
  startlocation = tables.Column(verbose_name= 'Start Position' )
  endlocation = tables.Column(verbose_name= 'End Position')
  regulated = tables.Column(verbose_name= 'Regulated' )

  class Meta:
    model = targetedgene
    attrs = {'class': 'paleblue', 'width':'150%'}
    fields = ('targetedgenes', 'fullnamegene', 'entrezgene', 'refseqgene', 'chromlocation', 'startlocation' , 'endlocation' , 'regulated' ) # fields to display










