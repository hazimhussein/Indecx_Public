# Generated by Django 4.2.6 on 2023-10-24 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_indecol', '0003_alter_project_keywords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='keywords',
            field=models.CharField(max_length=50),
        ),
    ]
