from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Case
import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import Evidence



def home(request):
    return render(request, 'dashboard.html')


#def getCaseData(request):
    cases = Case.objects.all()
    return render(
        request, 'listCases.html', {"cases":cases}
   )

def getCaseData(request):
    cases = Case.objects.prefetch_related('evidences').all()
    return render( request, 'listCases.html',{"cases": cases})


def getEvidence(request):
    return render(request, 'evidenceList.html')

def case_details(request, case_id):
    case = Case.objects.prefetch_related('evidences').get(id=case_id)
    evidences = case.evidences.all()
    return render(request, 'case_details.html', {"case":case, "evidences":evidences})

def add_evidence(request, case_id):
    if request.method == "POST":
        evidence_name = request.POST.get(
            "evidence_name"
        )
        uploaded_file = request.FILES.get(
            "evidence_file"
        )
        # Save file in media folder
        fs = FileSystemStorage()
        filename = fs.save(
            uploaded_file.name,
            uploaded_file
        )
        file_url = fs.url(filename)
        # Save in database
        Evidence.objects.create(
            case_id=case_id,
            evidence_name=evidence_name,
            file_name=uploaded_file.name,
            file_path=filename,
            file_type=uploaded_file.content_type
        )

        return render(request, "addEvidance.html",{"success": "File saved successfully"} )

    return render(request,"addEvidance.html")