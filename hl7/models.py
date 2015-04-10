from django.db import models

class Document(models.Model):
	docid = models.AutoField(primary_key=True)

class ComponentMSH(models.Model):
	text = models.TextField()
	doc = models.ForeignKey(Document)

class ComponentEVN(models.Model):
	text = models.TextField()
	doc = models.ForeignKey(Document)

class ComponentPID(models.Model):
	text = models.TextField()
	doc = models.ForeignKey(Document)

class ComponentPD1(models.Model):
	text = models.TextField()
	doc = models.ForeignKey(Document)

class ComponentNK1(models.Model):
	text = models.TextField()
	doc = models.ForeignKey(Document)

class ComponentPV1(models.Model):
	text = models.TextField()
	doc = models.ForeignKey(Document)# Create your models here.

class ComponentIN1(models.Model):
	text = models.TextField()
	doc = models.ForeignKey(Document)# Create your models here.
