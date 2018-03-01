# Generated by Django 2.0.2 on 2018-03-01 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0007_auto_20180301_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='description',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='platform',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='variant',
        ),
        migrations.AddField(
            model_name='patient',
            name='id_description',
            field=models.ForeignKey(db_column='id_description', null=True, on_delete=django.db.models.deletion.CASCADE, to='db.Description'),
        ),
        migrations.AddField(
            model_name='patient',
            name='id_platform',
            field=models.ForeignKey(db_column='id_platform', null=True, on_delete=django.db.models.deletion.CASCADE, to='db.Platform'),
        ),
        migrations.AddField(
            model_name='patient',
            name='id_variant',
            field=models.ForeignKey(db_column='id_variant', null=True, on_delete=django.db.models.deletion.CASCADE, to='db.Variant'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='id_stage',
            field=models.ForeignKey(db_column='id_stage', null=True, on_delete=django.db.models.deletion.CASCADE, to='db.Stage'),
        ),
    ]
