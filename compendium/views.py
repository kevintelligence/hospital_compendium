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

def details(request):
    try:
        key = request.GET['idnum']
    except():
        b = True
    c= Hospital.objects.raw('''SELECT id AS idnum, name AS name,  CONCAT(address, ' ', city, ' ', state, ' ', zipcode) AS address, phonenumber AS phonenumber, hospitaltype AS hospitaltype, emergency AS emergency, criteria AS meetcriteria, overallrating AS overallrating, mortalitycomparison AS mortalitycomparison, safetycomparison AS safetycomparison, readmissioncomparison AS readmissioncomparison, patientexperiencecomparison AS experiencecomparison, effectivenesscomparison AS effectivenesscomparison, timelinesscomparison AS timelinesscomparison, efficientimagingcomparison AS imagingcomparison FROM general WHERE id = ''' + key)
    hospital_info = []
    for a in c:
        hospital_info = [a.idnum, a.name, a.address, a.phonenumber, a.hospitaltype, a.emergency, a.meetcriteria, a.overallrating, a.mortalitycomparison, a.safetycomparison, a.readmissioncomparison, a.experiencecomparison, a.effectivenesscomparison, a.timelinesscomparison, a.imagingcomparison]
    
    hospital_info.append(Hospital.objects.raw('''SELECT starrating AS summarystar FROM patientsatisfaction WHERE question = "Summary star rating" AND id = ".key" ''').summarystar)
    hospital_info.append(Hospital.objects.raw('''SELECT starrating AS cleanlinessstar FROM patientsatisfaction WHERE question = "Cleanliness - star rating" AND id = .key ''').cleanlinessstar)
    hospital_info.append(Hospital.objects.raw('''SELECT starrating AS nursestar  FROM patientsatisfaction WHERE question = "Nurse communication - star rating" AND id = .key ''').nursestar)
    hospital_info.append(Hospital.objects.raw('''SELECT starrating AS doctorstar FROM patientsatisfaction WHERE question = ""Doctor communication - star rating AND id = .key ''').doctorstar)
    hospital_info.append(Hospital.objects.raw('''SELECT starrating AS staffstar FROM patientsatisfaction WHERE question = "Staff responsiveness - star rating" AND id = .key ''').staffstar)
    hospital_info.append(Hospital.objects.raw('''SELECT starrating AS communicationstar FROM patientsatisfaction WHERE question = "Communication about medicines - star rating" AND id = .key ''').communicationstar)
    hospital_info.append(Hospital.objects.raw('''SELECT starrating AS dischargestar FROM patientsatisfaction WHERE question = "Discharge information - star rating" AND id = .key''').dischargestar)
    hospital_info.append(Hospital.objects.raw('''SELECT starrating AS carestar FROM patientsatisfaction WHERE question = "Care transition - star rating" AND id = .key''').carestar)
    hospital_info.append(Hospital.objects.raw('''SELECT starrating AS overallstar FROM patientsatisfaction WHERE question = "Overall hospital rating - star rating" AND id = .key''').overallstar)
    hospital_info.append(Hospital.objects.raw('''SELECT starrating AS quietnessstar FROM patientsatisfaction WHERE question = "Quietness - star rating" AND id = .key''').quietnessstar)
    hospital_info.append(Hospital.objects.raw('''SELECT starrating AS recommendationstar FROM patientsatisfaction WHERE question = "Recommend hospital - star rating" AND id = .key''').recommendationstar)
    hospital_info.append(Hospital.objects.raw('''SELECT score AS hipknee FROM complication WHERE measure = "Rate of complications for hip/knee replacement patients" AND id = .key''').hipknee)
    hospital_info.append(Hospital.objects.raw('''SELECT score AS heartattack FROM complication WHERE measure = "Death rate for heart attack patients" AND id = .key''').heartattack)
    hospital_info.append(Hospital.objects.raw('''SELECT score AS CABG FROM complication WHERE measure = "Death rate for CABG surgery patients" AND id = .key''').CABG)
    hospital_info.append(Hospital.objects.raw('''SELECT score AS COPD FROM complication WHERE measure = "Death rate for chronic obstructive pulmonary disease (COPD) patients" AND id = .key''').COPD)
    hospital_info.append(Hospital.objects.raw('''SELECT score AS heartfailure FROM complication WHERE measure = "Death rate for heart failure patients" AND id = .key''').heartfailure)
    hospital_info.append(Hospital.objects.raw('''SELECT score AS pneumonia FROM complication WHERE measure = "Death rate for pneumonia patients" AND id = .key''').pneumonia)
    hospital_info.append(Hospital.objects.raw('''SELECT score AS stroke FROM complication WHERE measure = "Death rate for stroke patients" AND id = .key''').stroke)
    hospital_info.append(Hospital.objects.raw('''SELECT score AS kidney FROM complication WHERE measure = "Postoperative Acute Kidney Injury Requiring Dialysis Rate" AND id = .key''').kidney)
    hospital_info.append(Hospital.objects.raw('''SELECT score AS respiratoryfailure FROM complication WHERE measure = "Postoperative Respiratory Failure Rate" AND id = .key''').respiratoryfailure)
    hospital_info.append(Hospital.objects.raw('''SELECT score AS bloodclot FROM complication WHERE measure = "Serious blood clots after surgery" AND id = .key''').bloodclot)
    hospital_info.append(Hospital.objects.raw('''SELECT score AS bloodstream FROM complication WHERE measure = "Blood stream infection after surgery" AND id = .key''').bloodstream)
    hospital_info.append(Hospital.objects.raw('''SELECT score AS wound FROM complication FROM complication WHERE measure = "A wound that splits open  after surgery on the abdomen or pelvis" AND id = .key''').wound)
    hospital_info.append(Hospital.objects.raw('''SELECT score AS tear FROM complication WHERE measure = "Accidental cuts and tears from medical treatment" AND id = .key''').tear)
    hospital_info.append(Hospital.objects.raw('''SELECT score AS sore FROM complication WHERE measure = "Pressure sores" AND id = .key''').sore)
    hospital_info.append(Hospital.objects.raw('''SELECT score AS serioustreatable FROM complication WHERE measure = "Deaths among Patients with Serious Treatable Complications after Surgery" AND id = .key''').serioustreatable)
    hospital_info.append(Hospital.objects.raw('''SELECT score AS collapsedlung FROM complication WHERE measure = "Collapsed lung due to medical treatment" AND id = .key''').collapsedlung)
    hospital_info.append(Hospital.objects.raw('''SELECT score AS brokenhip FROM complication WHERE measure = "Broken hip from a fall after surgery" AND id = .key''').brokenship)
    hospital_info.append(Hospital.objects.raw('''SELECT score AS hemorrhage FROM complication WHERE measure = "Perioperative Hemorrhage or Hematoma Rate" AND id = .key''').hemorrhage)
    hospital_info.append(Hospital.objects.raw('''SELECT score AS seriouscomplications FROM complication WHERE measure = "Serious complications" AND id = .key''').seriouscomplications)
    hospital_info.append(Hospital.objects.raw('''SELECT comparison AS hipkneecomparison FROM complication WHERE measure = "Rate of complications for hip/knee replacement patients" AND id = .key''').hipkneecomparison)
    hospital_info.append(Hospital.objects.raw('''SELECT comparison AS heartattackcomparison FROM complication WHERE measure = "Death rate for heart attack patients" AND id = .key''').heartattackcomparison)
    hospital_info.append(Hospital.objects.raw('''SELECT comparison AS CABGcomparison FROM complication WHERE measure = "Death rate for CABG surgery patients" AND id = .key''').CABG)
    hospital_info.append(Hospital.objects.raw('''SELECT comparison AS COPDcomparison FROM complication WHERE measure = "Death rate for chronic obstructive pulmonary disease (COPD) patients" AND id = .key''').COPDcomparison)
    hospital_info.append(Hospital.objects.raw('''SELECT comparison AS heartfailurecomparison FROM complication WHERE measure = "Death rate for heart failure patients" AND id = .key''').heartfailurecomparison)
    hospital_info.append(Hospital.objects.raw('''SELECT comparison AS pneumoniacomparison FROM complication WHERE measure = "Death rate for pneumonia patients" AND id = .key''').pneumoniacomparison)
    hospital_info.append(Hospital.objects.raw('''SELECT comparison AS strokecomparison FROM complication WHERE measure = "Death rate for stroke patients" AND id = .key''').strokecomparisoncomparison)
    hospital_info.append(Hospital.objects.raw('''SELECT comparison AS kidneycomparison FROM complication WHERE measure = "Postoperative Acute Kidney Injury Requiring Dialysis Rate" AND id = .key''').kidneycomparison)
    hospital_info.append(Hospital.objects.raw('''SELECT comparison AS respiratoryfailurecomparison FROM complication WHERE measure = "Postoperative Respiratory Failure Rate" AND id = .key''').respiratoryfailurecomparison)
    hospital_info.append(Hospital.objects.raw('''SELECT comparison AS bloodclotcomparison FROM complication WHERE measure = "Serious blood clots after surgery" AND id = .key''').bloodclotcomparison)
    hospital_info.append(Hospital.objects.raw('''SELECT comparison AS bloodstreamcomparison FROM complication WHERE measure = "Blood stream infection after surgery" AND id = .key''').bloodstreamcomparison)
    hospital_info.append(Hospital.objects.raw('''SELECT comparison AS woundcomparison FROM complication WHERE measure = "A wound that splits open  after surgery on the abdomen or pelvis" AND id = .key''').woundcomparison)
    hospital_info.append(Hospital.objects.raw('''SELECT comparison AS tearcomparison FROM complication WHERE measure = "Accidental cuts and tears from medical treatment" AND id = .key''').tearcomparison)
    hospital_info.append(Hospital.objects.raw('''SELECT comparison AS sorecomparison FROM complication WHERE measure = "Pressure sores" AND id = .key''').sorecomparison)
    hospital_info.append(Hospital.objects.raw('''SELECT comparison AS serioustreatablecomparison FROM complication WHERE measure = "Deaths among Patients with Serious Treatable Complications after Surgery" AND id = .key''').serioustreatablecomparison)
    hospital_info.append(Hospital.objects.raw('''SELECT comparison AS collapsedlungcomparison FROM complication WHERE measure = "Collapsed lung due to medical treatment" AND id = .key''').collapsedlungcomparison)
    hospital_info.append(Hospital.objects.raw('''SELECT comparison AS brokenhipcomparison FROM complication WHERE measure = "Broken hip from a fall after surgery" AND id = .key''').brokenshipcomparison)
    hospital_info.append(Hospital.objects.raw('''SELECT comparison AS hemorrhagecomparison FROM complication WHERE measure = "Perioperative Hemorrhage or Hematoma Rate" AND id = .key''').hemorrhagecomparison)
    hospital_info.append(Hospital.objects.raw('''SELECT comparison AS seriouscomplicationscomparison FROM complication WHERE measure = "Serious complications" AND id = .key''').seriouscomplicationscomparison)
    hospital_info.append(Hospital.objects.raw('''SELECT sd AS hipkneesd FROM complication WHERE measure = "Rate of complications for hip/knee replacement patients" AND id = .key''').hipkneesd)
    hospital_info.append(Hospital.objects.raw('''SELECT sd AS heartattacksd FROM complication WHERE measure = "Death rate for heart attack patients" AND id = .key''').heartattacksd)
    hospital_info.append(Hospital.objects.raw('''SELECT sd AS CABGsd FROM complication WHERE measure = "Death rate for CABG surgery patients" AND id = .key''').CABGsd)
    hospital_info.append(Hospital.objects.raw('''SELECT sd AS COPDsd FROM complication WHERE measure = "Death rate for chronic obstructive pulmonary disease (COPD) patients" AND id = .key''').COPDsd)
    hospital_info.append(Hospital.objects.raw('''SELECT sd AS heartfailuresd FROM complication WHERE measure = "Death rate for heart failure patients" AND id = .key''').heartfailuresd)
    hospital_info.append(Hospital.objects.raw('''SELECT sd AS pneumoniasd FROM complication WHERE measure = "Death rate for pneumonia patients" AND id = .key''').pneumoniasd)
    hospital_info.append(Hospital.objects.raw('''SELECT sd AS strokesd FROM complication WHERE measure = "Death rate for stroke patients" AND id = .key''').strokecomparisonsd)
    hospital_info.append(Hospital.objects.raw('''SELECT sd AS kidneysd FROM complication WHERE measure = "Postoperative Acute Kidney Injury Requiring Dialysis Rate" AND id = .key''').kidneysd)
    hospital_info.append(Hospital.objects.raw('''SELECT sd AS respiratoryfailuresd FROM complication WHERE measure = "Postoperative Respiratory Failure Rate" AND id = .key''').respiratorysd)
    hospital_info.append(Hospital.objects.raw('''SELECT sd AS bloodclotsd FROM complication WHERE measure = "Serious blood clots after surgery" AND id = .key''').bloodclotsd)
    hospital_info.append(Hospital.objects.raw('''SELECT sd AS bloodstreamsd FROM complication WHERE measure = "Blood stream infection after surgery" AND id = .key''').bloodstreamsd)
    hospital_info.append(Hospital.objects.raw('''SELECT sd AS woundsd FROM complication WHERE measure = "A wound that splits open  after surgery on the abdomen or pelvis" AND id = .key''').woundsd)
    hospital_info.append(Hospital.objects.raw('''SELECT sd AS tearsd FROM complication WHERE measure = "Accidental cuts and tears from medical treatment" AND id = .key''').tearsd)
    hospital_info.append(Hospital.objects.raw('''SELECT sd AS soresd FROM complication WHERE measure = "Pressure sores" AND id = .key''').soresd)
    hospital_info.append(Hospital.objects.raw('''SELECT sd AS serioustreatablesd FROM complication WHERE measure = "Deaths among Patients with Serious Treatable Complications after Surgery" AND id = .key''').serioustreatablesd)
    hospital_info.append(Hospital.objects.raw('''SELECT sd AS collapsedlungsd FROM complication WHERE measure = "Collapsed lung due to medical treatment" AND id = .key''').collapsedlungsd)
    hospital_info.append(Hospital.objects.raw('''SELECT sd AS brokenhipsd FROM complication WHERE measure = "Broken hip from a fall after surgery" AND id = .key''').brokenshipsd)
    hospital_info.append(Hospital.objects.raw('''SELECT sd AS hemorrhagesd FROM complication WHERE measure = "Perioperative Hemorrhage or Hematoma Rate" AND id = .key''').hemorrhagesd)
    hospital_info.append(Hospital.objects.raw('''SELECT sd AS seriouscomplicationssd FROM complication WHERE measure = "Serious complications" AND id = .key''').seriouscomplicationssd)
    hospital_info.append(Hospital.objects.raw('''SELECT ed AS hipkneeed FROM complication WHERE measure = "Rate of complications for hip/knee replacement patients" AND id = .key''').hipkneeed)
    hospital_info.append(Hospital.objects.raw('''SELECT ed AS heartattacked FROM complication WHERE measure = "Death rate for heart attack patients" AND id = .key''').heartattacked)
    hospital_info.append(Hospital.objects.raw('''SELECT ed AS CABGed FROM complication WHERE measure = "Death rate for CABG surgery patients" AND id = .key''').CABGed)
    hospital_info.append(Hospital.objects.raw('''SELECT ed AS COPDed FROM complication WHERE measure = "Death rate for chronic obstructive pulmonary disease (COPD) patients" AND id = .key''').COPDed)
    hospital_info.append(Hospital.objects.raw('''SELECT ed AS heartfailureed FROM complication WHERE measure = "Death rate for heart failure patients" AND id = .key''').heartfailuresded)
    hospital_info.append(Hospital.objects.raw('''SELECT ed AS pneumoniaed FROM complication WHERE measure = "Death rate for pneumonia patients" AND id = .key''').pneumoniaed)
    hospital_info.append(Hospital.objects.raw('''SELECT ed AS strokeed FROM complication WHERE measure = "Death rate for stroke patients" AND id = .key''').strokecomparisoned)
    hospital_info.append(Hospital.objects.raw('''SELECT ed AS kidneyed FROM complication WHERE measure = "Postoperative Acute Kidney Injury Requiring Dialysis Rate" AND id = .key''').kidneyed)
    hospital_info.append(Hospital.objects.raw('''SELECT ed AS respiratoryfailureed FROM complication WHERE measure = "Postoperative Respiratory Failure Rate" AND id = .key''').respiratoryed)
    hospital_info.append(Hospital.objects.raw('''SELECT ed AS bloodcloted FROM complication WHERE measure = "Serious blood clots after surgery" AND id = .key''').bloodcloted)
    hospital_info.append(Hospital.objects.raw('''SELECT ed AS bloodstreamed FROM complication WHERE measure = "Blood stream infection after surgery" AND id = .key''').bloodstreamed)
    hospital_info.append(Hospital.objects.raw('''SELECT ed AS wounded FROM complication WHERE measure = "A wound that splits open  after surgery on the abdomen or pelvis" AND id = .key''').wounded)
    hospital_info.append(Hospital.objects.raw('''SELECT ed AS teared FROM complication WHERE measure = "Accidental cuts and tears from medical treatment" AND id = .key''').teared)
    hospital_info.append(Hospital.objects.raw('''SELECT ed AS soreed FROM complication WHERE measure = "Pressure sores" AND id = .key''').soreed)
    hospital_info.append(Hospital.objects.raw('''SELECT ed AS serioustreatableed FROM complication WHERE measure = "Deaths among Patients with Serious Treatable Complications after Surgery" AND id = .key''').serioustreatableed)
    hospital_info.append(Hospital.objects.raw('''SELECT ed AS collapsedlunged FROM complication WHERE measure = "Collapsed lung due to medical treatment" AND id = .key''').collapsedlunged)
    hospital_info.append(Hospital.objects.raw('''SELECT ed AS brokenhiped FROM complication WHERE measure = "Broken hip from a fall after surgery" AND id = .key''').brokenshiped)
    hospital_info.append(Hospital.objects.raw('''SELECT ed AS hemorrhageed FROM complication WHERE measure = "Perioperative Hemorrhage or Hematoma Rate" AND id = .key''').hemorrhageed)
    hospital_info.append(Hospital.objects.raw('''SELECT ed AS seriouscomplicationsed FROM complication WHERE measure = "Serious complications" AND id = .key''').seriouscomplicationsed)
    hospital_info.append(Hospital.objects.raw('''SELECT he AS heartattackpayh FROM value WHERE measure = "PAYM_30_AMI" AND id = .key''').heartattackpayh)
    hospital_info.append(Hospital.objects.raw('''SELECT he AS heartfailurepayh FROM value WHERE measure = "PAYM_30_HF" AND id = .key''').heartfailurpayh)
    hospital_info.append(Hospital.objects.raw('''SELECT he AS hipkneepayh FROM value WHERE measure = "PAYM_90_HIP_KNEE" AND id = .key''').hipkneepayh)
    hospital_info.append(Hospital.objects.raw('''SELECT he AS pneumoniapayh FROM value WHERE measure = "PAYM_30_PN" AND id = .key''').pneumoniapayh)
    hospital_info.append(Hospital.objects.raw('''SELECT le AS heartattackpayl FROM value WHERE measure = "PAYM_30_AMI" AND id = .key''').heartattackpayl)
    hospital_info.append(Hospital.objects.raw('''SELECT le AS heartfailurepayl FROM value WHERE measure = "PAYM_30_HF" AND id = .key''').heartfailurepayl)
    hospital_info.append(Hospital.objects.raw('''SELECT le AS hipkneepayl FROM value WHERE measure = "PAYM_90_HIP_KNEE" AND id = .key''').hipkneepayl)
    hospital_info.append(Hospital.objects.raw('''SELECT le AS pneumoniapayl FROM value WHERE measure = "PAYM_30_PN" AND id = .key''').pneumoniapayl)
    hospital_info.append(Hospital.objects.raw('''SELECT value AS heartattackvalue FROM value WHERE measure = "PAYM_30_AMI" AND id = .key''').heartattackvalue)
    hospital_info.append(Hospital.objects.raw('''SELECT value AS heartfailurevalue FROM value WHERE measure = "PAYM_30_HF" AND id = .key''').heartfailurevalue)
    hospital_info.append(Hospital.objects.raw('''SELECT value AS hipkneevalue FROM value WHERE measure = "PAYM_90_HIP_KNEE" AND id = .key''').hipkneevalue)
    hospital_info.append(Hospital.objects.raw('''SELECT value AS pneumoniavalue FROM value WHERE measure = "PAYM_30_PN" AND id = .key''').pneumoniavalue)
    hospital_info.append(Hospital.objects.raw('''SELECT comparison AS heartattackcomparison FROM value WHERE measure = "PAYM_30_AMI" AND id = .key''').heartattackcomparison)
    hospital_info.append(Hospital.objects.raw('''SELECT comparison AS heartfailurecomparison FROM value WHERE measure = "PAYM_30_HF" AND id = .key''').heartfailurecomparison)
    hospital_info.append(Hospital.objects.raw('''SELECT comparison AS hipkneecomparison FROM value WHERE measure = "PAYM_90_HIP_KNEE" AND id = .key''').hipkneecomparison)
    hospital_info.append(Hospital.objects.raw('''SELECT comparison AS pneumoniacomparison FROM value WHERE measure = "PAYM_30_PN" AND id = .key''').pneumoniacomparison)
    template = loader.get_template("details.html")
    print(hospital_info)
    context = {
        'a' : hospital_info
    }
    return HttpResponse(template.render(context, request))











