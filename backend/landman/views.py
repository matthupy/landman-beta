from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AcreageTypeSerializer, AcreageSerializer, AddressSerializer, AgreementStageSerializer, AgreementStatusSerializer, AgreementTypeSerializer, AgreementSerializer, BackupWithholdingTypeSerializer, BusinessAssociateTypeSerializer, CountySerializer, CountrySerializer, EntityTypeSerializer, JeffLegalHeaderSerializer, LandDivisionSerializer, LandownerSerializer, NoteSerializer, ProjectProgressDateStatusSerializer, ProjectProgressDateTypeSerializer, ProjectProgressDateSerializer, ProjectSerializer, RightSerializer, StateSerializer, SubjectTypeSerializer, SurveyTypeSerializer, TaskStatusSerializer, TaskSerializer, UnitSerializer, WellStatusSerializer, WellSerializer, WorkingListSerializer
from .models import AcreageType, Acreage, Address, AgreementStage, AgreementStatus, AgreementType, Agreement, BackupWithholdingType, BusinessAssociateType, County, Country, EntityType, JeffLegalHeader, LandDivision, Landowner, Note, ProjectProgressDateStatus, ProjectProgressDateType, ProjectProgressDate, Project, Right, State, SubjectType, SurveyType, TaskStatus, Task, Unit, WellStatus, Well, WorkingList

# Create your views here.

class AcreageTypeView(viewsets.ModelViewSet):
    serializer_class = AcreageTypeSerializer
    queryset = AcreageType.objects.all()

class AcreageView(viewsets.ModelViewSet):
    serializer_class = AcreageSerializer
    queryset = Acreage.objects.all()

class AddressView(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

class AgreementStageView(viewsets.ModelViewSet):
    serializer_class = AgreementStageSerializer
    queryset = AgreementStage.objects.all()

class AgreementStatusView(viewsets.ModelViewSet):
    serializer_class = AgreementStatusSerializer
    queryset = AgreementStatus.objects.all()

class AgreementTypeView(viewsets.ModelViewSet):
    serializer_class = AgreementTypeSerializer
    queryset = AgreementType.objects.all()

class AgreementView(viewsets.ModelViewSet):
    serializer_class = AgreementSerializer
    queryset = Agreement.objects.all()

class BackupWithholdingTypeView(viewsets.ModelViewSet):
    serializer_class = BackupWithholdingTypeSerializer
    queryset = BackupWithholdingType.objects.all()

class BusinessAssociateTypeView(viewsets.ModelViewSet):
    serializer_class = BusinessAssociateTypeSerializer
    queryset = BusinessAssociateType.objects.all()

class CountyView(viewsets.ModelViewSet):
    serializer_class = CountySerializer
    queryset = County.objects.all()

class CountryView(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

class EntityTypeView(viewsets.ModelViewSet):
    serializer_class = EntityTypeSerializer
    queryset = EntityType.objects.all()

class JeffLegalHeaderView(viewsets.ModelViewSet):
    serializer_class = JeffLegalHeaderSerializer
    queryset = JeffLegalHeader.objects.all()

class LandDivisionView(viewsets.ModelViewSet):
    serializer_class = LandDivisionSerializer
    queryset = LandDivision.objects.all()

class LandownerView(viewsets.ModelViewSet):
    serializer_class = LandownerSerializer
    queryset = Landowner.objects.all()

class NoteView(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

class ProjectProgressDateStatusView(viewsets.ModelViewSet):
    serializer_class = ProjectProgressDateStatusSerializer
    queryset = ProjectProgressDateStatus.objects.all()

class ProjectProgressDateTypeView(viewsets.ModelViewSet):
    serializer_class = ProjectProgressDateTypeSerializer
    queryset = ProjectProgressDateType.objects.all()

class ProjectProgressDateView(viewsets.ModelViewSet):
    serializer_class = ProjectProgressDateSerializer
    queryset = ProjectProgressDate.objects.all()

class ProjectView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class RightView(viewsets.ModelViewSet):
    serializer_class = RightSerializer
    queryset = Right.objects.all()

class StateView(viewsets.ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()

class SubjectTypeView(viewsets.ModelViewSet):
    serializer_class = SubjectTypeSerializer
    queryset = SubjectType.objects.all()

class SurveyTypeView(viewsets.ModelViewSet):
    serializer_class = SurveyTypeSerializer
    queryset = SurveyType.objects.all()

class TaskStatusView(viewsets.ModelViewSet):
    serializer_class = TaskStatusSerializer
    queryset = TaskStatus.objects.all()

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class UnitView(viewsets.ModelViewSet):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()

class WellStatusView(viewsets.ModelViewSet):
    serializer_class = WellStatusSerializer
    queryset = WellStatus.objects.all()

class WellView(viewsets.ModelViewSet):
    serializer_class = WellSerializer
    queryset = Well.objects.all()

class WorkingListView(viewsets.ModelViewSet):
    serializer_class = WorkingListSerializer
    queryset = WorkingList.objects.all()