# Generated by Django 4.2.6 on 2023-11-24 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_indecol', '0006_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ressource',
            new_name='Resource',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='ressources',
            new_name='resources',
        ),
    ]
