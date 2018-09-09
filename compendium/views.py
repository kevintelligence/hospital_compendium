from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Hospital

# Create your views here.
def index(request):
    hospital_list = Hospital.objects.raw('''SELECT id AS idnum, name AS name, CONCAT(address, ' ', city, ' ', state, ' ', zipcode) AS address, phonenumber AS phonenumber, hospitaltype AS hospitaltype, emergency AS emergency, criteria AS meetcriteria,  overallrating AS overallrating FROM general''')
    hospital_info = []
    for a in hospital_list:
        hospital_info.append([a.idnum, a.name.title(), a.address.title(), a.phonenumber, a.hospitaltype, a.overallrating])
    template = loader.get_template("index.html")
    context = {
        'hospital_info' : hospital_info
    }
    return HttpResponse(template.render(context, request))

#def details(request):