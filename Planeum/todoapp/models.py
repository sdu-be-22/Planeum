from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.

class Job(models.Model):
    jobName = models.CharField(max_length = 200, verbose_name = 'Job Name', default = '')
    dateAdded = models.DateTimeField(verbose_name='Time', default = datetime.now)
    isCompleted = models.BooleanField(default = False)

    def __str__(self):
        return self.jobName + ' - ' + self.dateAdded + ' - ' + str(self.isCompleted)
