from django.contrib import admin

from hl7.models import *

admin.site.register(Document)
admin.site.register(ComponentMSH)
admin.site.register(ComponentEVN)
admin.site.register(ComponentPID)
admin.site.register(ComponentPD1)
admin.site.register(ComponentNK1)
admin.site.register(ComponentPV1)
admin.site.register(ComponentIN1)
admin.site.register(Record)

# Register your models here.
