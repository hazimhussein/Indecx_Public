# Generated by Django 4.2.6 on 2023-12-21 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_indecol', '0011_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
