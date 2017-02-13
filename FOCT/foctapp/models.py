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



