# Generated by Django 5.1.2 on 2024-11-07 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0018_seekerprofilemodel_skill_jobmodel_applyjobmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruiterprofilemodel',
            name='company_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]