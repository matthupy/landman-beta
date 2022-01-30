from django.contrib.auth.models import User
from django.db import models

from .ProjectProgressDateStatus import ProjectProgressDateStatus
from .ProjectProgressDateType import ProjectProgressDateType

class ProjectProgressDate(models.Model):
    type = models.ForeignKey(ProjectProgressDateType, on_delete=models.PROTECT)
    status = models.ForeignKey(ProjectProgressDateStatus, on_delete=models.PROTECT)
    due_date = models.DateField(verbose_name="Due Date")
    completed_date = models.DateField(verbose_name="Completed Date")
    assigned_to = models.ForeignKey(User, on_delete=models.PROTECT, related_name="assigned_to")
    update_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="update_user")
    update_date = models.DateTimeField()