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
from landman.views import *

router = routers.DefaultRouter()
router.register(r'acreage/types', AcreageTypeView)
router.register(r'acreages', AcreageView)
router.register(r'addresses', AddressView)
router.register(r'agreement/stages', AgreementStageView)
router.register(r'agreement/statuses', AgreementStatusView)
router.register(r'agreement/types', AgreementTypeView)
router.register(r'agreements', AgreementView)
router.register(r'backupwithholdingtypes', BackupWithholdingTypeView)
router.register(r'businessassociatetypes', BusinessAssociateTypeView)
router.register(r'counties', CountyView)
router.register(r'countries', CountryView)
router.register(r'entitytypes', EntityTypeView)
router.register(r'jefflegalheader', JeffLegalHeaderView)
router.register(r'landdivisions', LandDivisionView)
router.register(r'landowners', LandownerView)
router.register(r'notes', NoteView)
router.register(r'project/progressdate/statuses', ProjectProgressDateStatusView)
router.register(r'project/progressdate/types', ProjectProgressDateTypeView)
router.register(r'project/progressdate', ProjectProgressDateView)
router.register(r'project', ProjectView)
router.register(r'rights', RightView)
router.register(r'states', StateView)
router.register(r'subjecttypes', SubjectTypeView)
router.register(r'surveytypes', SurveyTypeView)
router.register(r'task/status', TaskStatusView)
router.register(r'tasks', TaskView)
router.register(r'units', UnitView)
router.register(r'well/status', WellStatusView)
router.register(r'wells', WellView)
router.register(r'workinglist', WorkingListView)

urlpatterns = [
    path('', RedirectView.as_view(url='/api/')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
