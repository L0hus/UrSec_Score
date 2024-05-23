from django.shortcuts import render
from django.http import HttpResponse
from User.models import Report
from User.forms import reportForm
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from loguru import logger

def index(request):
    return render(request, "index.html")

def report(request):
    report_Form = reportForm()
    return render(request, "reports.html", {"form": report_Form})

def test(request):
    form_report = reportForm(request.POST, request.FILES)
    if request.method == "POST":
        img = request.FILES.get("activCertif")
        filename = img.name
        fs = FileSystemStorage()
        filename = fs.save('media/user_cert/' + filename, img)
        logger.debug(filename)
        time = datetime.strptime(form_report.data["activDate"],"%Y-%m-%d").date()
        report = Report.objects.create(activName = form_report.data["activName"], 
                        activDate = time, 
                        activCertif = img)
        
    # activ_Name = request.POST.get("activName", "")
    # activ_Date = request.POST.get("activDate", 1)
    # activ_Link = request.POST.get("activLink", "")
    # activ_Place = request.POST.get("activPlace", "")
    # activ_Certif = request.POST.get("activCertif")
    # activ_Other = request.POST.get("activOther", "")
    # activ_Addit = request.POST.get("activAddit", "")
    return HttpResponse(f"""
                        <p>Мероприятие: {form_report.data["activName"]}</p>
                        <p>Дата мероприятия: {form_report.data["activDate"]}</p>
                        <img src="/{filename}">
                        """)
