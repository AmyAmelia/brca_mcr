# Generated by Django 2.0.2 on 2018-03-01 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0008_auto_20180301_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='stage',
            field=models.CharField(max_length=3, null=True, unique=True),
        ),
    ]