from django.urls import path

from . import views


urlpatterns = [

    path('', views.home),
    path('cases/',views.getCaseData,name="getCaseData"),
    path('evidence/',views.getEvidence,name="getEvidence"),
    #path('add_evidence/',views.add_evidence,name="add_evidence"),
    path('add-evidence/<int:case_id>/', views.add_evidence, name='add_evidence'),
    path('case-details/<int:case_id>/', views.case_details, name='case_details')

]
