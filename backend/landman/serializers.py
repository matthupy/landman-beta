from rest_framework import serializers
from .models import AcreageType, Acreage, Address, AgreementStage, AgreementStatus, AgreementType, Agreement, BackupWithholdingType, BusinessAssociateType, County, Country, EntityType, JeffLegalHeader, LandDivision, Landowner, Note, ProjectProgressDateStatus, ProjectProgressDateType, ProjectProgressDate, Project, Right, State, SubjectType, SurveyType, TaskStatus, Task, Unit, WellStatus, Well, WorkingList

class AcreageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcreageType
        fields = ('code', 'description')

class AcreageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acreage
        fields = ('type', 'amount', 'unit', 'agreement')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('attention_line1', 'attention_line2', 'address_line1', 'address_line2', 'city', 'state', 'zip')

class AgreementStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgreementStage
        fields = ('code', 'description', 'index')

class AgreementStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgreementStatus
        fields = ('code', 'description')

class AgreementTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgreementType
        fields = ('code', 'category', 'description')

class AgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = ('name', 'number', 'type', 'status', 'stage', 'landDivision', 'originalLessee', 'agreementDate', 'effectiveDate', 'term', 'rights', 'related', 'wells')

class BackupWithholdingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackupWithholdingType
        fields = ('code', 'description')

class BusinessAssociateTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessAssociateType
        fields = ('code', 'description')

class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = ('id', 'state', 'code', 'name', 'update_date', 'update_user','hidden')

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'code', 'abbreviation', 'name', 'update_date', 'update_user','hidden')

class EntityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityType
        fields = ('code', 'description')

class JeffLegalHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = JeffLegalHeader
        fields = ('country','state','county','townshipNum','townshipDir','rangeNum','rangeDir','section')

class LandDivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandDivision
        fields = ('code','description')

class LandownerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landowner
        fields = ('name', 'entity_type', 'address', 'email', 'ssn', 'backupWithholdingType', 'backupWithholding')

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('text', 'update_user', 'update_date')

class ProjectProgressDateStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectProgressDateStatus
        fields = ('code','description')

class ProjectProgressDateTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectProgressDateType
        fields = ('code','description')

class ProjectProgressDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectProgressDate
        fields = ('type','status','due_date','completed_date','assigned_to','update_user','update_date')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name','number','description','type','status','stage','country','state','county','tasks','contacts','cross_refferences','progress_dates')

class RightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Right
        fields = ('code','description')

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('country','code','abbreviation','name','survey','update_date','update_user','hidden')

class SurveyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyType
        fields = ('code','description')

class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = ('code','description')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name','type','status','effDateFrom','effDateTo','dueDate')

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('code','description')

class WellStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = WellStatus
        fields = ('code','description')

class WellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Well
        fields = ('name','status','latitude','longitude')

class WorkingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingList
        fields = ('user','agreements')

class SubjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectType
        fields = ('code', 'description')