from django.db import models


class Patient(models.Model):
    id_patient = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField(null=True)
    id_stage = models.ForeignKey('Stage', on_delete=models.CASCADE, db_column='id_stage', null=True)
    id_description = models.ForeignKey('Description', on_delete=models.CASCADE, db_column='id_description', null=True)
    id_platform = models.ForeignKey('Platform', on_delete=models.CASCADE, db_column='id_platform', null=True)
    id_variant = models.ForeignKey('Variant', on_delete=models.CASCADE, db_column='id_variant', null=True)
    class Meta:
        db_table = 'patient'
    def __unicode__(self):
        return u'{0}'.format(self.name)


class Stage(models.Model):
    id_stage = models.AutoField(primary_key=True)
    stage = models.CharField(max_length=3, null=True, unique=True)
    stage_str = models.CharField(max_length=10, null=True, unique=True)
    class Meta:
        db_table = 'stage'
    def __unicode__(self):
        return u'{0}'.format(self.stage)


class Description(models.Model):
    id_description = models.AutoField(primary_key=True)
    description = models.CharField(max_length=20, unique=True)
    class Meta:
        db_table = 'description'
    def __unicode__(self):
        return u'{0}'.format(self.description)


class Platform(models.Model):
    id_platform = models.AutoField(primary_key=True)
    platform = models.CharField(max_length=30, unique=True)
    class Meta:
        db_table = 'platform'
    def __unicode__(self):
        return u'{0}'.format(self.platform)


class Variant(models.Model):
    id_variant = models.AutoField(primary_key=True)
    cdna = models.CharField(max_length=100, unique=False)
    protein = models.CharField(max_length=100, unique=False)
    genomic = models.CharField(max_length=100, unique=False)
    rsid =  models.CharField(max_length=100, null=True, unique=False)
    polyphen = models.CharField(max_length=100,null=True,  unique=False)
    sift = models.CharField(max_length=100, null=True, unique=False)
    gnomad_af = models.CharField(max_length=100, null=True, unique=False)
    class Meta:
        db_table = 'variant'
    def __unicode__(self):
        return u'{0}'.format(self.cdna)
