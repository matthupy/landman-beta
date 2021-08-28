"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from rest_framework import routers
from landman import views

router = routers.DefaultRouter()
router.register(r'acreage/types', views.AcreageTypeView)
router.register(r'acreages', views.AcreageView)
router.register(r'addresses', views.AddressView)
router.register(r'agreement/stages', views.AgreementStageView)
router.register(r'agreement/statuses', views.AgreementStatusView)
router.register(r'agreement/types', views.AgreementTypeView)
router.register(r'agreements', views.AgreementView)
router.register(r'backupwithholdingtypes', views.BackupWithholdingTypeView)
router.register(r'businessassociatetypes', views.BusinessAssociateTypeView)
router.register(r'counties', views.CountyView)
router.register(r'countries', views.CountryView)
router.register(r'entitytypes', views.EntityTypeView)
router.register(r'jefflegalheader', views.JeffLegalHeaderView)
router.register(r'landdivisions', views.LandDivisionView)
router.register(r'landowners', views.LandownerView)
router.register(r'notes', views.NoteView)
router.register(r'project/progressdate/statuses', views.ProjectProgressDateStatusView)
router.register(r'project/progressdate/types', views.ProjectProgressDateTypeView)
router.register(r'project/progressdate', views.ProjectProgressDateView)
router.register(r'project', views.ProjectView)
router.register(r'rights', views.RightView)
router.register(r'states', views.StateView)
router.register(r'subjecttypes', views.SubjectTypeView)
router.register(r'surveytypes', views.SurveyTypeView)
router.register(r'task/status', views.TaskStatusView)
router.register(r'tasks', views.TaskView)
router.register(r'units', views.UnitView)
router.register(r'well/status', views.WellStatusView)
router.register(r'wells', views.WellView)
router.register(r'workinglist', views.WorkingListView)

urlpatterns = [
    path('', RedirectView.as_view(url='/api/')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
