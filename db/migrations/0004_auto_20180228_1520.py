# Generated by Django 2.0.2 on 2018-02-28 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_auto_20180227_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='cdna',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='variant',
            name='genomic',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='variant',
            name='protein',
            field=models.CharField(max_length=30),
        ),
    ]
