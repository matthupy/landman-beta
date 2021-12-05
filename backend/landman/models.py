from enum import unique
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime
from simple_history.models import HistoricalRecords
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.
class LandDivision(models.Model):
    code = models.CharField(max_length=3)
    description = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.description}"

    class Meta:
        verbose_name = "Land Division"
        verbose_name_plural = "Land Divisions"

class SurveyType(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    description = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Survey Type"
        verbose_name_plural = "Survey Types"

    def __str__(self):
        return f"{self.description}"

class Note(models.Model):
    text = models.TextField()
    update_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    update_date = models.DateTimeField()

    def __str__(self):
        return f"ID # {self.id} ({self.update_user}, {self.update_date})"

class ProjectProgressDateType(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    description = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Project Progress Date Type"
        verbose_name_plural = "Project Progress Date Types"

    def __str__(self):
        return f"{self.description}"

class ProjectProgressDateStatus(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    description = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Project Progress Date Status"
        verbose_name_plural = "Project Progress Date Statuses"

    def __str__(self):
        return f"{self.description}"

class ProjectProgressDate(models.Model):
    type = models.ForeignKey(ProjectProgressDateType, on_delete=models.PROTECT)
    status = models.ForeignKey(ProjectProgressDateStatus, on_delete=models.PROTECT)
    due_date = models.DateField(verbose_name="Due Date")
    completed_date = models.DateField(verbose_name="Completed Date")
    assigned_to = models.ForeignKey(User, on_delete=models.PROTECT, related_name="assigned_to")
    update_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="update_user")
    update_date = models.DateTimeField()

class Country(models.Model):
    code = models.CharField(max_length=4)
    abbreviation = models.CharField(max_length=3)
    name = models.CharField(max_length=50)
    update_date = models.DateField()
    update_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    hidden = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return f"{self.abbreviation} | {self.name}"

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    code = models.CharField(max_length=6)
    abbreviation = models.CharField(max_length=3)
    name = models.CharField(max_length=50)
    survey = models.ForeignKey(SurveyType, on_delete=models.PROTECT)
    update_date = models.DateField()
    update_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.abbreviation} | {self.name}"

class County(models.Model):
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=50)
    update_date = models.DateField()
    update_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "County"
        verbose_name_plural = "Counties"

class BusinessAssociateType(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    description = models.CharField(max_length=40)

    class Meta:
        verbose_name = "Business Associate Type"
        verbose_name_plural = "Business Associate Types"

    def __str__(self):
        return f"{self.code} | {self.description}"

class EntityType(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    description = models.CharField(max_length=128)

    class Meta:
        verbose_name = "Entity Type"
        verbose_name_plural = "Entity Types"

    def __str__(self):
        return f"{self.code} | {self.description}"

class ProjectStatus(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    description = models.CharField(max_length=128)

    class Meta:
        verbose_name = "Project Status"
        verbose_name_plural = "Project Statuses"

    def __str__(self):
        return f"{self.code} | {self.description}"

class ProjectStage(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    description = models.CharField(max_length=128)
    index = models.IntegerField(unique=True)

    class Meta:
        verbose_name = "Project Stage"
        verbose_name_plural = "Project Stages"

    def __str__(self):
        return f"{self.code} | {self.description} ({self.index})"

class ProjectType(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    description = models.CharField(max_length=128)

    class Meta:
        verbose_name = "Project Type"
        verbose_name_plural = "Project Types"

    def __str__(self):
        return f"{self.code} | {self.description}"


class TaskStatus(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    description = models.CharField(max_length=128)

    class Meta:
        verbose_name = "Task Status"
        verbose_name_plural = "Task Statuses"

    def __str__(self):
        return f"{self.code} | {self.description}"

class TaskType(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    description = models.CharField(max_length=128)

    class Meta:
        verbose_name = "Task Type"
        verbose_name_plural = "Task Types"

    def __str__(self):
        return f"{self.code} | {self.description}"

class BackupWithholdingType(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    description = models.CharField(max_length=40)

    class Meta:
        verbose_name = "Backup Withholding Type"
        verbose_name_plural = "Backup Withholding Types"

    def __str__(self):
        return f"{self.code} | {self.description}"

class Address(models.Model):
    attention_line1 = models.CharField(max_length=128, blank=True)
    attention_line2 = models.CharField(max_length=128, blank=True)
    address_line1 = models.CharField(max_length=128)
    address_line2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    zip = models.CharField(max_length=5)

    def __str__(self):
        rtn = ""
        if (self.attention_line1):
            rtn = f"{rtn}ATTN: {self.attention_line1}"
        if (self.attention_line2):
            rtn = f"{rtn} {self.attention_line2}"
        if (self.address_line1):
            rtn = f"{rtn} {self.address_line1}"
        if (self.address_line2):
            rtn = f"{rtn} {self.address_line2}"
        if (self.city):
            rtn = f"{rtn} {self.city}"
        if (self.state):
            rtn = f"{rtn}, {self.state.abbreviation}"
        if (self.zip):
            rtn = f"{rtn} {self.zip}"
        return rtn

class Task(models.Model):
    name = models.CharField(max_length=254)
    type = models.ForeignKey(TaskType, on_delete=models.PROTECT)
    status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT)
    effDateFrom = models.DateField(verbose_name="Effective Date From", blank=True)
    effDateTo = models.DateField(verbose_name="Effective Date To", blank=True)
    dueDate = models.DateField(verbose_name="Due Date", blank=True)
    history = HistoricalRecords()

    def validate_effective_dates(self):
        """
            Validates that the effective date to is greater than the effective date from
        """
        print('into task validation')
        print('validation should be {0}'.format(self.effDateFrom <= self.effDateTo))
        if (self.effDateFrom <= self.effDateTo):
            return True
        else: return False

    def clean(self):
        # Make sure that the effective date to is after effective date from
        test_result = self.effDateFrom <= self.effDateTo
        if (not test_result):
            raise ValidationError('Effective Date To cannot be before or equal to Effective Date From')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs) # Call the real save event

    def __str__(self):
        return f"{self.name} ({self.status})"

class Landowner(models.Model):
    name = models.CharField(max_length=128)
    entity_type = models.ForeignKey(EntityType, on_delete=models.PROTECT)
    address = models.ManyToManyField(Address)
    email = models.EmailField(max_length=254)
    ssn = models.CharField(max_length=11, blank=False, verbose_name="Social Security Number")
    backupWithholdingType = models.ForeignKey(BackupWithholdingType, on_delete=models.PROTECT)
    backupWithholding = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def __str__(self):
        return f"{self.name}"

class Project(models.Model):
    name = models.CharField(max_length=128)
    number = models.CharField(max_length=128)
    description = models.TextField()
    type = models.ForeignKey(ProjectType, on_delete=models.PROTECT)
    status = models.ForeignKey(ProjectStatus, on_delete=models.PROTECT)
    stage = models.ForeignKey(ProjectStage, on_delete=models.PROTECT)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    county = models.ForeignKey(County, on_delete=models.PROTECT)
    tasks = models.ManyToManyField(Task, blank=True)
    contacts = models.ManyToManyField(Landowner, blank=True)
    cross_references = models.ManyToManyField('self', blank=True)
    progress_dates = models.ManyToManyField(ProjectProgressDate, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.id} - {self.name}"

class AgreementStatus(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    description = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.code} : {self.description}"

    class Meta:
        verbose_name = "Agreement Status"
        verbose_name_plural = "Agreement Statuses"

class AgreementStage(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    description = models.CharField(max_length=128)
    index = models.IntegerField(unique=True)

    class Meta:
        verbose_name = "Agreement Stage"
        verbose_name_plural = "Agreement Stages"

    def __str__(self):
        return f"{self.code} | {self.description} ({self.index})"
class Right(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    description = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.code} : {self.description}"

class SubjectType(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    description = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.code} : {self.description}"

    class Meta:
        verbose_name = "Subject Type"
        verbose_name_plural = "Subject Types"

class AcreageType(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    description = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.code} : {self.description}"

    class Meta:
        verbose_name = "Acreage Type"
        verbose_name_plural = "Acreage Types"

class Unit(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    description = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.code} : {self.description}"

class AgreementType(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    category = models.ForeignKey(SubjectType, on_delete=models.PROTECT, related_name='agreement_types')
    description = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.category.code}-{self.code} : {self.description}"

    class Meta:
        verbose_name = "Agreement Type"
        verbose_name_plural = "Agreement Types"

class WellStatus(models.Model):
    code = models.CharField(max_length=3)
    description = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.description}"

    class Meta:
        verbose_name = "Well Status"
        verbose_name_plural = "Well Statuses"

class Well(models.Model):
    name = models.CharField(max_length=40)
    status = models.ForeignKey(WellStatus, on_delete=models.PROTECT)
    latitude = models.DecimalField(decimal_places=15, max_digits= 18, default=0)
    longitude = models.DecimalField(decimal_places=15, max_digits= 18, default=0)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.name} ({self.status.description})"

class Agreement(models.Model):
    name = models.CharField(max_length=40)
    number = models.CharField(max_length=40)
    type = models.ForeignKey(AgreementType, on_delete=models.PROTECT)
    status = models.ForeignKey(AgreementStatus, on_delete=models.PROTECT)
    stage = models.ForeignKey(AgreementStage, on_delete=models.PROTECT)
    landDivision = models.ForeignKey(LandDivision, on_delete=models.PROTECT)
    originalLessee = models.CharField(max_length=40)
    agreementDate = models.DateField()
    effectiveDate = models.DateField()
    term = models.IntegerField(null=False)
    rights = models.ForeignKey(Right, on_delete=models.PROTECT)
    related = models.ManyToManyField('self', blank=True)
    wells = models.ManyToManyField(Well, blank=True)
    history = HistoricalRecords()

    def inactivate(self):
        from landman.models import AgreementStatus
        if (self.status == AgreementStatus.objects.filter(code="IN").first()):
            return False
        else:
            self.status = AgreementStatus.objects.filter(code="IN").first()
            self.save()

    def reactivate(self):
        from landman.models import AgreementStatus
        if (self.status == AgreementStatus.objects.filter(code="A").first()):
            return False
        else:
            self.status = AgreementStatus.objects.filter(code="A").first()
            self.save()

    def __str__(self):
        return f"{self.number} - {self.name}"

class LegalSegment(models.Model):
    agreement = models.ForeignKey(Agreement, related_name='legal_segments', on_delete=models.PROTECT)
    surveyType = models.ForeignKey(SurveyType, on_delete=models.PROTECT)
    acreage = models.DecimalField(decimal_places=6, max_digits=13, blank=True, null=True)

    class Meta:
        abstract = True

class JeffLegalHeader(LegalSegment):
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    state = ChainedForeignKey(State
                                    , chained_field="country"
                                    , chained_model_field="country"
                                    , show_all=False
                                    , auto_choose=True
                                    , on_delete=models.PROTECT)
    county = ChainedForeignKey(County
                                    , chained_field="state"
                                    , chained_model_field="state"
                                    , show_all=False
                                    , auto_choose=True
                                    , on_delete=models.PROTECT)
    townshipNum = models.IntegerField(blank=False)
    townshipDir = models.CharField(max_length=10, choices=[('N','North'),('S','South')], blank=False, default='N')
    rangeNum = models.IntegerField(blank=False)
    rangeDir = models.CharField(max_length=10, choices=[('E','East'),('W','West')], blank=False, default='E')
    section = models.IntegerField(blank=False)
    history = HistoricalRecords()

    def validate_country_state_county(self):
        """
            Validates that the Country/State/County configuration is valid, meaning the selected county
            is tied to the selected state, and the selected state is tied to the selected country
        """
        if (self.county.state == self.state and self.state.country == self.country):
            return True
        else: return False

    def __str__(self):
        township = 'T' + ('{:03}'.format(self.townshipNum)) + self.townshipDir
        range = 'R' + ('{:03}'.format(self.rangeNum)) + self.rangeDir
        section = 'S' + ('{:03}'.format(self.section))
        return f"ID #{self.id}: {self.country.code} / {self.state.abbreviation} / {self.county.name} / {township} / {range} / {section}"

    def save(self, *args, **kwargs):
        if (self.validate_country_state_county()):
            super().save(*args, **kwargs) # Call the real save event

    class Meta:
        verbose_name = "Jeffersonian Legal Segment"
        verbose_name_plural = "Jeffersonian Legal Segments"

class Acreage(models.Model):
    type = models.ForeignKey(AcreageType, on_delete=models.PROTECT)
    amount = models.DecimalField(decimal_places=2, max_digits=9, default=0)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)
    agreement = models.ForeignKey(Agreement, on_delete=models.CASCADE, related_name='acreage', blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.agreement.number} - {self.type.description} - {self.amount} {self.unit.description}"

class WorkingList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    agreements = models.ManyToManyField(Agreement, blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.agreements.count()})"