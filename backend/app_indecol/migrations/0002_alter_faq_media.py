# Generated by Django 4.2.6 on 2024-02-15 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_indecol', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='media',
            field=models.FileField(null=True, upload_to='media/'),
        ),
    ]
