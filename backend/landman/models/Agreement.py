from django.db import models
from simple_history.models import HistoricalRecords

from .AgreementStage import AgreementStage
from .AgreementStatus import AgreementStatus
from .AgreementType import AgreementType
from .LandDivision import LandDivision
from .Right import Right
from .Well import Well

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