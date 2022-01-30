from django.db import models

from .Agreement import Agreement
from .SurveyType import SurveyType

class LegalSegment(models.Model):
    agreement = models.ForeignKey(Agreement, related_name='legal_segments', on_delete=models.PROTECT)
    surveyType = models.ForeignKey(SurveyType, on_delete=models.PROTECT)
    acreage = models.DecimalField(decimal_places=6, max_digits=13, blank=True, null=True)

    class Meta:
        abstract = True