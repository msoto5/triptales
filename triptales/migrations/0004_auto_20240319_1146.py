# Generated by Django 2.2.28 on 2024-03-19 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triptales', '0003_auto_20240319_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacationpost',
            name='title',
            field=models.CharField(default='Trip to <django.db.models.query_utils.DeferredAttribute object at 0x794d64ffed30>, <django.db.models.query_utils.DeferredAttribute object at 0x794d64ff77c0>', max_length=128),
        ),
    ]