# Generated by Django 4.2.6 on 2023-10-25 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_indecol", "0010_ressource"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ressource",
            name="project",
        ),
        migrations.AddField(
            model_name="project",
            name="ressources",
            field=models.ManyToManyField(to="app_indecol.ressource"),
        ),
    ]
