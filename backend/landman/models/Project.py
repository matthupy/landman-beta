from django.db import models
from simple_history.models import HistoricalRecords

from .Country import Country
from .County import County
from .Landowner import Landowner
from .ProjectProgressDate import ProjectProgressDate
from .ProjectStage import ProjectStage
from .ProjectStatus import ProjectStatus
from .ProjectType import ProjectType
from .State import State
from .Task import Task


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