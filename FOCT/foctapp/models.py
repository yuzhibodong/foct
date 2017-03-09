from django.db import models


# Create your models here.
class Abstractfoct(models.Model):
    #����
    name=models.CharField(max_length=20)
    #��λ��
    phase_error=models.FloatField()
    #�Ȳ�
    current_error=models.FloatField()
    #�⹦��
    light_power=models.FloatField()
    #һ�ε�����Чֵ
    rated_primary_current=models.FloatField()
    #REF��Чֵ
    ref=models.FloatField()
    #�������
    composite_error=models.FloatField()
    #����
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





