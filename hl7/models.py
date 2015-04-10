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

###All the above are defunct, ignore.
class Record(models.Model):
    msh_9 = models.TextField()
    msh_10 = models.TextField()
    msh_11 = models.TextField()
    msh_12 = models.TextField()
    pid_5 = models.TextField()
    pid_11 = models.TextField()
    evn_2 = models.TextField()
    evn_4 = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
    	return u'Record created at %s' % (self.date_added)

