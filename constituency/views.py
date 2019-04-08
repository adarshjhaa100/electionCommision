from django.shortcuts import get_object_or_404
from django.http import HttpResponse,JsonResponse
from . models import suggest,Result,pollingStation,voter,pwd_voter,Candidate,loc
from django.core import serializers
import json
import base64
from django.http import JsonResponse


def UpdateNo(request):
	no=request.GET['z']
	n=request.GET['n']
	p=pollingStation.objects.filter(Pid=n).update(people=no)
	return HttpResponse(str(n))

#for main app

#search polling station
def SearchStation(request):
	ep=request.GET['e']
	q=get_object_or_404(voter,epicNo=ep)
	data={}
	data['Pid']=q.station.Pid
	return JsonResponse(data,safe=False)


#Get Details of all
def GetAll(request):
	q=pollingStation.objects.all()
	data=[]
	for a in q:
		p={}
		p['Pid']=a.Pid
		p['people']=a.people
		data.append(p)
	#print (data)	
	return JsonResponse(data,safe=False)	

#get details with epic no
def GetDetails(request):
	n=request.GET['n']
	q=pollingStation.objects.get(Pid=n)
	data={}
	data['Pid']=q.Pid
	data['people']=q.people
	return JsonResponse(data)


def registerNo(request):
	v=voter.objects.all()
	for i in v:
		if (i.category=='PWD' or i.category=='THRD') and i.const=='Chandni Chowk':
			m=pwd_voter(epicNo=i.epicNo,const=i.const,station=i.station,category=i.category)
			m.save()
		
	e=request.GET['e']
	n=request.GET['p']

	for r in pwd_voter.objects.all():
		if pwd_voter.objects.filter(epicNo=r.epicNo).count()>1:
			r.delete()		
	l=pwd_voter.objects.filter(epicNo=e).update(ph=n)
   	
	n=pwd_voter.objects.get(epicNo=e)
	return JsonResponse({'success':True})

def give(request):
	e=request.GET['e']
	lat=request.GET['x']
	lon=request.GET['y']
	n=pwd_voter.objects.get(epicNo=e)

	x=loc.objects.filter(stn=n.station)
	
	a=[]
	for i in x:
		a.append(((i.lat),(i.lon),((i.lat-float(lat))**2+(i.lon-float(lon))**2)))
	def k(ele):
		return ele[2]	
	a.sort(key=k)
	b=[]
	for i in a:
		data={}
		data['lat']=i[0]
		data['lon']=i[1]
		data['pickupTime']=n.pick	
		data['DropTime']=n.drop
		b.append(data)
	y=pwd_voter.objects.filter(epicNo=e).update(plat=a[0][0],plon=a[0][1])	
	return JsonResponse(b,safe=False)

def getCandidate(request):
	p=request.GET['p']
	q=Candidate.objects.get(party=p)
	a=base64.encodestring(q.symbol.read())
	return HttpResponse(a)


def sugg(request):
	suggestion=request.GET['s']
	review=request.GET['r']
	s=suggest(suggestion=suggestion,rating=review)
	s.save()
	a=[]
	return HttpResponse(suggestion+','+str(review))


def DisplayResults(request):
	r=Result.objects.all()
	arr=[]
	for a in r:
		data={}
		data['name']=a.name
		data['votes']=a.no
		arr.append(data)
	return JsonResponse(arr,safe=False)			

