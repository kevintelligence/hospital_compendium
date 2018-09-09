from django.db import models

# Create your models here.
class Hospital(models.Model):
    # General
    idnum = models.IntegerField(primary_key=True)
    name = models.TextField
    address = models.TextField
    phonenumber = models.IntegerField
    hospitaltype = models.TextField
    emergency = models.CharField
    meetcriteria = models.CharField
    overallrating = models.CharField
    mortalitycomparison = models.CharField
    safetycomparison = models.CharField
    readmissioncomparison = models.CharField
    experiencecomparison = models.CharField
    effectivenesscomparison = models.CharField
    timelinesscomparison = models.CharField
    imagingcomparison = models.CharField

    # Patient Satisfaction
    summarystar = models.CharField
    cleanlinessstar = models.CharField
    nursestar = models.CharField
    doctorstar = models.CharField
    staffstar = models.CharField
    communicationstar = models.CharField
    dischargestar = models.CharField
    carestarstar = models.CharField
    overallstar = models.CharField
    quietnessstar = models.CharField
    recommendationstar = models.CharField

    # Complications and deaths
    hipknee = models.TextField
    heartattack = models.TextField
    CABG = models.TextField
    COPD = models.TextField
    heartfailure = models.TextField
    pneumonia = models.TextField
    stroke = models.TextField
    kidney = models.TextField
    respiratoryfailure = models.TextField
    bloodclot = models.TextField
    bloodstream = models.TextField
    wound = models.TextField
    tear = models.TextField
    sore = models.TextField
    serioustreatable = models.TextField
    collapsedlung = models.TextField
    brokenhip = models.TextField
    hemorrhage = models.TextField
    seriouscomplications = models.TextField

    hipkneecomparison = models.TextField
    heartattackcomparison = models.TextField
    CABGcomparison = models.TextField
    COPDcomparison = models.TextField
    heartfailurecomparison = models.TextField
    pneumoniacomparison = models.TextField
    strokecomparison = models.TextField
    kidneycomparison = models.TextField
    respiratoryfailurecomparison = models.TextField
    bloodclotcomparison = models.TextField
    bloodstreamcomparison = models.TextField
    woundcomparison = models.TextField
    tearcomparison = models.TextField
    sorecomparison = models.TextField
    serioustreatablecomparison = models.TextField
    collapsedlungcomparison = models.TextField
    brokenhipcomparison = models.TextField
    hemorrhagecomparison = models.TextField
    seriouscomplicationscomparison = models.TextField

    hipkneesd = models.TextField
    heartattacksd = models.TextField
    CABGsd = models.TextField
    COPDsd = models.TextField
    heartfailuresd = models.TextField
    pneumoniasd = models.TextField
    strokesd = models.TextField
    kidneysd = models.TextField
    respiratoryfailuresd = models.TextField
    bloodclotsd = models.TextField
    bloodstreamsd = models.TextField
    woundsd = models.TextField
    tearsd = models.TextField
    soresd = models.TextField
    serioustreatablesd = models.TextField
    collapsedlungsd = models.TextField
    brokenhipsd = models.TextField
    hemorrhagesd = models.TextField
    seriouscomplicationssd = models.TextField

    hipkneeed = models.TextField
    heartattacked = models.TextField
    CABGed = models.TextField
    COPDed = models.TextField
    heartfailureed = models.TextField
    pneumoniaed = models.TextField
    strokeed = models.TextField
    kidneyed = models.TextField
    respiratoryfailureed = models.TextField
    bloodcloted = models.TextField
    bloodstreamed = models.TextField
    wounded = models.TextField
    teared = models.TextField
    soreed = models.TextField
    serioustreatableed = models.TextField
    collapsedlunged = models.TextField
    brokenhiped = models.TextField
    hemorrhageed = models.TextField
    seriouscomplicationsed = models.TextField

    #Payment and Value
    heartattackpayh = models.TextField
    heartfailurepayh = models.TextField
    hipkneepayh = models.TextField
    pneumoniapayh = models.TextField

    heartattackpayl = models.TextField
    heartfailurepayl = models.TextField
    hipkneepayl = models.TextField
    pneumoniapayl = models.TextField

    heartattackvalue = models.TextField
    heartfailurevalue = models.TextField
    hipkneevalue = models.TextField
    pneumoniavalue = models.TextField

    heartattackcomparison = models.TextField
    heartfailurecomparison = models.TextField
    hipkneecomparison = models.TextField
    pneumoniacomparison = models.TextField