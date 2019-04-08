from django.urls import path
from . import views

app_name='constituency'

urlpatterns=[
#searches pollingstation alloted to a voter
path('searchS/',views.SearchStation,name='station'),
#update no of people in queue
path('updateQ/',views.UpdateNo,name='updateq'),
#add suggestion
path('suggestion/',views.sugg,name='sugg'),
#display results
path('displayR/',views.DisplayResults,name='displayR'),
#get details of pollingstation with id
path('getDetails/',views.GetDetails,name='gtD'),
#register number
path('register/',views.registerNo,name='reg'),
path('getC/',views.getCandidate,name='getCandidate'),
path('getAll/',views.GetAll,name='g'),
#search for nearest pickup
path('givel/',views.give,name='give')

]
