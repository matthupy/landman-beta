from django import forms
from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from simple_history.admin import SimpleHistoryAdmin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter
from .models import *

class AgreementHistoryAdmin(SimpleHistoryAdmin):
    list_display = ("number","name","agreement_status","agreement_type","agreement_rights","well_count")
    list_filter = ("status","type","rights")
    search_fields  = ("number__contains","name__contains")

    def agreement_status(self, obj):
        from landman.models import AgreementStatus
        status = AgreementStatus.objects.get(code=obj.status.code)
        return status.description

    def agreement_type(self,obj):
        from landman.models import AgreementType
        type = AgreementType.objects.get(code=obj.type.code)
        return type.description

    def agreement_rights(self,obj):
        from landman.models import Right
        rights = Right.objects.get(code=obj.rights.code)
        return rights.description

    def well_count(self, obj):
        return obj.wells.count()

class CountryAdmin(admin.ModelAdmin):
    ## Actions
    def make_hidden(self, request, queryset):
        queryset.update(hidden=True)
    make_hidden.short_description = 'Hide selected countries'

    def make_unhidden(self, request, queryset):
        queryset.update(hidden=False)
    make_unhidden.short_description = 'Un-Hide selected countries'

    list_display = ("id","code","abbreviation","name","hidden","state_count")
    search_fields = ("abbreviation__contains","name__contains")
    list_filter = (("name", ChoiceDropdownFilter),
                    "hidden")
    ordering = ['abbreviation']
    actions = [make_hidden, make_unhidden]

    def state_count(self,obj):
        return obj.state_set.all().count()

class CountyAdmin(admin.ModelAdmin):
    list_display = ("id","country_name","state_code","state_name","code","name","hidden")
    search_fields = ("id","name__contains","code__contains")
    list_filter = (("state__country", RelatedDropdownFilter),
                   ("state", RelatedDropdownFilter),
                    "hidden")
    ordering = ["state","name"]

    def country_name(self,obj):
        return obj.state.country.name

    def state_name(self,obj):
        return obj.state.name

    def state_code(self,obj):
        return obj.state.code

class JeffLegalHeaderForm(forms.ModelForm):
    class Meta:
        model = JeffLegalHeader
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(JeffLegalHeaderForm, self).__init__(*args, **kwargs)
        self.fields['country'].queryset = Country.objects.filter(hidden=False)

class JeffLegalHeaderHistoryAdmin(SimpleHistoryAdmin):
    list_display = ("id","agreement_number","country_name","state_name","county_name","township_num", "townshipDir", "range_num", "rangeDir", "section_num", "acreage")
    search_fields = ("id","agreement__name__contains","agreement__number__contains")
    list_filter = (("country", RelatedDropdownFilter),
                   ("state", RelatedDropdownFilter),
                   ("county", RelatedDropdownFilter))
    ordering = ["country","state","county", "townshipDir","townshipNum","rangeDir","rangeNum","section"]

    form = JeffLegalHeaderForm

    def agreement_number(self,obj):
        return obj.agreement.number

    def agreement_name(self,obj):
        return obj.agreement.name

    def country_name(self,obj):
        return obj.country.name

    def state_name(self,obj):
        return obj.state.name

    def county_name(self,obj):
        return obj.county.name

    def township_num(self,obj):
        return '{:03}'.format(obj.townshipNum)

    def range_num(self,obj):
        return '{:03}'.format(obj.rangeNum)

    def section_num(self,obj):
        return '{:03}'.format(obj.section)

class StateAdmin(admin.ModelAdmin):
    ## Actions
    def make_hidden(self, request, queryset):
        queryset.update(hidden=True)
    make_hidden.short_description = 'Hide selected states'

    def make_unhidden(self, request, queryset):
        queryset.update(hidden=False)
    make_unhidden.short_description = 'Un-Hide selected states'

    list_display = ("id","country_name","code","abbreviation","name","hidden","county_count")
    search_fields = ("abbreviation__contains","name__contains","code")
    list_filter = (("country", RelatedDropdownFilter),
                   ("survey", RelatedDropdownFilter),
                    "hidden")
    ordering = ["country","abbreviation"]
    actions = [make_hidden, make_unhidden]

    def country_name(self,obj):
        return obj.country.name

    def county_count(self,obj):
        return obj.county_set.all().count()

class TaskHistoryAdmin(SimpleHistoryAdmin):
    list_display = ("id","name","task_type","task_status","effDateFrom","effDateTo","dueDate")
    list_filter = ("type","status")
    search_fields = ("id","name__contains")

    def task_status(self,obj):
        return obj.status.description

    def task_type(self,obj):
        return obj.type.description

# Register your models here.

## CODE TABLES
admin.site.register(Acreage)
admin.site.register(AcreageType)
admin.site.register(Address)
admin.site.register(AgreementStage)
admin.site.register(AgreementStatus)
admin.site.register(AgreementType)
admin.site.register(BackupWithholdingType)
admin.site.register(BusinessAssociateType)
admin.site.register(EntityType)
admin.site.register(LandDivision)
admin.site.register(Landowner)
admin.site.register(Note)
admin.site.register(Project)
admin.site.register(ProjectProgressDate)
admin.site.register(ProjectProgressDateStatus)
admin.site.register(ProjectProgressDateType)
admin.site.register(ProjectStage)
admin.site.register(ProjectStatus)
admin.site.register(ProjectType)
admin.site.register(Right)
admin.site.register(SubjectType)
admin.site.register(SurveyType)
admin.site.register(TaskType)
admin.site.register(TaskStatus)
admin.site.register(Unit)
admin.site.register(WellStatus)
admin.site.register(Well, SimpleHistoryAdmin)
admin.site.register(WorkingList)

admin.site.register(Agreement, AgreementHistoryAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(County, CountyAdmin)
admin.site.register(JeffLegalHeader, JeffLegalHeaderHistoryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Task, TaskHistoryAdmin)