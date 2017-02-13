from django.db import models


# Create your models here.
class Abstractfoct(models.Model):
    #名称
    name=models.CharField(max_length=20)
    #相位差
    phase_error=models.FloatField()
    #比差
    current_error=models.FloatField()
    #光功率
    light_power=models.FloatField()
    #一次电流有效值
    rated_primary_current=models.FloatField()
    #REF有效值
    ref=models.FloatField()
    #复合误差
    composite_error=models.FloatField()
    #日期
    test_time=models.DateField()
    class Meta:
        abstract=True

class Foct(Abstractfoct):
    max_temperature=models.CharField(max_length=10)
    min_temperature=models.CharField(max_length=10)
    def __unicode__(self):
        return self.name
class Collector(Abstractfoct):
    foct=models.ForeignKey(Foct)
    def __unicode__(self):
        return self.name



