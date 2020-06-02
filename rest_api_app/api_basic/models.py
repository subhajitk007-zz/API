import pytz
from django.db import models
from timezone_field import TimeZoneField
# Create your models here.

class User(models.Model):

    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    id = models.CharField(max_length=9,primary_key=True)
    real_name = models.CharField(max_length=255)
    tz = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')
    def __str__(self):
        return self.real_name

class ActivityPeriod(models.Model):
    users = models.ForeignKey(User, related_name='activity_periods', on_delete=models.CASCADE, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    def __str__(self):
        return '%s: %s' % (self.start_time, self.end_time)

    # class Meta:
    #     unique_together = ['users', 'start_time','end_time']