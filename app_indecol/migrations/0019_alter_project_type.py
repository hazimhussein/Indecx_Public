# Generated by Django 4.2.6 on 2023-10-25 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_indecol', '0018_alter_project_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('M', 'Master Project'), ('PhD', 'PhD Project'), ('PD', 'PostDoc Project'), ('O', 'Other type'), ('EU', 'European Project')], default='-', max_length=50),
        ),
    ]
