# Generated by Django 4.2.6 on 2024-02-22 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_indecol', '0005_alter_person_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.FileField(null=True, upload_to='media/'),
        ),
    ]
