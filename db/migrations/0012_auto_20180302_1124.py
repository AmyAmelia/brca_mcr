# Generated by Django 2.0.2 on 2018-03-02 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0011_auto_20180301_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='variant',
            name='gnomad_af',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='polyphen',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='rsid',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='sift',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
