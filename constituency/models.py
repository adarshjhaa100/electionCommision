from django.db import models
from django.utils.text import slugify
import django.utils.timezone

def user_path(instance,filename):
	return 'name_{0}/{1}'.format(instance, filename)

class pollingStation(models.Model):
	Pid=models.CharField(max_length=100,default='aaaa')
	photo=models.ImageField(upload_to=user_path)
	lat=models.FloatField(default=0.0)
	lon=models.FloatField(default=0.0)
	people=models.IntegerField(default=0)
	def __str__(self):
		return self.Pid

class facility(models.Model):
	fname=models.CharField(max_length=100)
	station=models.ForeignKey(pollingStation,on_delete=models.CASCADE)
	def __str__(self):
		return self.fname

class voter(models.Model):
	epicNo=models.CharField(max_length=10,default='null')
	const=models.CharField(max_length=30)
	station=models.ForeignKey(pollingStation,on_delete=models.CASCADE)
	category=models.CharField(max_length=5,default='GEN')
	def __str__(self):
		return self.epicNo

class pwd_voter(models.Model):
	epicNo=models.CharField(max_length=10,default='null')
	const=models.CharField(max_length=20)
	station=models.ForeignKey(pollingStation,on_delete=models.CASCADE)
	#PWD,THRD
	category=models.CharField(max_length=4,default='PWD')
	ph=models.BigIntegerField(default=0)
	plat=models.FloatField(default=0.0)
	plon=models.FloatField(default=0.0)
	pick=models.DateTimeField(default=django.utils.timezone.now)	
	drop=models.DateTimeField(default=django.utils.timezone.now)
	link=models.CharField(max_length=500,default='')
	def __str__(self):
		return self.epicNo

class loc(models.Model):
	lat=models.FloatField(default=0.0)
	lon=models.FloatField(default=0.0)
	stn=models.ForeignKey(pollingStation,on_delete=models.CASCADE)
	def __str__(self):
		return str(self.lat)+','+str(self.lon)
class Candidate(models.Model):
	name=models.CharField(max_length=50)
	party=models.CharField(max_length=10)
	symbol=models.ImageField(upload_to=user_path)
	affitavid=models.ImageField(upload_to=user_path)
	image=models.ImageField(upload_to=user_path,blank=True)
	def __str__(self):
		return self.name

class suggest(models.Model):
	suggestion=models.CharField(max_length=250)
	rating=models.IntegerField(default=0)
	
			
class Result(models.Model):
	name=models.CharField(max_length=100)
	no=models.IntegerField(default=0)
	def __str__(self):
		return self.name
