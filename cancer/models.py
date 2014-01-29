from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class cancer(models.Model):
	cancertype = models.CharField(max_length=150)
	subtype = models.CharField(max_length=150)
	cellline = models.CharField(max_length=150)

	def __unicode__(self):
		return self.cancertype + "  .  " + self.subtype + "  .  " + self.cellline



class smads(models.Model):
	cellline = models.CharField(max_length=150)
	smadtype = models.CharField(max_length=150)
	targetedgenes = models.CharField(max_length=150)

	def __unicode__(self):
		return self.cellline+ "  .  " + self.smadtype+ "  .  " + self.targetedgenes


class targetedgene(models.Model):
	targetedgenes = models.CharField(max_length=150)
	fullnamegene = models.CharField(max_length=150)
	entrezgene = models.IntegerField(max_length=150)
	refseqgene = models.CharField(max_length=150)
	chromlocation = models.IntegerField(max_length=10)
	startlocation = models.IntegerField(max_length=50)
	endlocation = models.IntegerField(max_length=50)
	regulated = models.CharField(max_length=10)

	def __unicode__(self):
		return self.targetedgenes+ "  .  " + self.fullnamegene + "  .  " + self.regulated

class item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()