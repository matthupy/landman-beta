from rest_framework import serializers
from landman.models import AcreageType, Acreage, Address, AgreementStage, AgreementStatus, AgreementType, Agreement, BackupWithholdingType, BusinessAssociateType, County, Country, EntityType, JeffLegalHeader, LandDivision, Landowner, Note, ProjectProgressDateStatus, ProjectProgressDateType, ProjectProgressDate, Project, Right, State, SubjectType, SurveyType, TaskStatus, Task, Unit, WellStatus, Well, WorkingList

class ProjectProgressDateTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectProgressDateType
        fields = ('code','description')