from rest_framework import viewsets
from landman.serializers import AcreageTypeSerializer, AcreageSerializer, AddressSerializer, AgreementStageSerializer, AgreementStatusSerializer, AgreementTypeSerializer, AgreementSerializer, BackupWithholdingTypeSerializer, BusinessAssociateTypeSerializer, CountySerializer, CountrySerializer, EntityTypeSerializer, JeffLegalHeaderSerializer, LandDivisionSerializer, LandownerSerializer, NoteSerializer, ProjectProgressDateStatusSerializer, ProjectProgressDateTypeSerializer, ProjectProgressDateSerializer, ProjectSerializer, RightSerializer, StateSerializer, SubjectTypeSerializer, SurveyTypeSerializer, TaskStatusSerializer, TaskSerializer, UnitSerializer, WellStatusSerializer, WellSerializer, WorkingListSerializer
from landman.models import AcreageType

class AcreageTypeView(viewsets.ModelViewSet):
    serializer_class = AcreageTypeSerializer
    queryset = AcreageType.objects.all()