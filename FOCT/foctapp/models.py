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
    test_time=models.DateField(auto_now=True)
    class Meta:
        abstract=True

class Foct(Abstractfoct):
    max_temperature=models.CharField(max_length=10)
    min_temperature=models.CharField(max_length=10)
    foct_testimage=models.ImageField(upload_to='foctapp',default='null')
    def __unicode__(self):
        return self.name
class Collector(Abstractfoct):
    foct=models.ForeignKey(Foct)
    temperature_data=models.FileField
    def __unicode__(self):
        return self.name

class Mirror(models.Model):
    name=models.CharField(max_length=100)
    reflectivity=models.FloatField()
    fsj_lenth=models.FloatField()
    fsj_producter=models.CharField(max_length=20)
    fsj_testproject=models.CharField(max_length=20)
    fsj_recoder=models.CharField(max_length=20)
    fsj_number=models.CharField(max_length=20)
    current_error=models.ImageField(upload_to='')
    test_time=models.DateField(auto_now=True)





