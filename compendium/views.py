from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Hospital

# Create your views here.
def index(request):
    hospital_list = Hospital.objects.raw('''SELECT id AS idnum, name AS name, CONCAT(address, city, state, zipcode) AS address, phonenumber AS phonenumber, hospitaltype AS hospitaltype, emergency AS emergency, criteria AS meetcriteria,  overallrating AS overallrating FROM general''')
    for a in hospital_list:
        print(a.name.title())
    template = loader.get_template("index.html")
    context = {
        'hospital_list' : hospital_list
    }
    return HttpResponse(template.render(context, request))

def details(request):
