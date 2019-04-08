from django.contrib import admin
from . models import facility,suggest,Result,voter,pollingStation,pwd_voter,Candidate,loc


class facilityInLine(admin.TabularInline):
	model=facility
	extra=0
class voterInLine(admin.TabularInline):
	model=voter
	extra=0

class pwd_voterInLine(admin.StackedInline):
	model=pwd_voter
	extra=0

class locInLine(admin.TabularInline):
	model=loc
	extra=0

class PollAdmin(admin.ModelAdmin):
	fieldsets=[
		(None,{'fields':['Pid']}),
		(None,{'fields':['photo']}),
		
		('location',{'fields':['lat']}),
		(None,{'fields':['lon']}),
		('No of people',{'fields':['people']})
	]
	inlines=[facilityInLine,voterInLine,pwd_voterInLine,locInLine]



admin.site.register(suggest)
admin.site.register(Result)
admin.site.register(pollingStation,PollAdmin)
admin.site.register(Candidate)
