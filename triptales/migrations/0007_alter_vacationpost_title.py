# Generated by Django 3.2.13 on 2024-03-21 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triptales', '0006_alter_vacationpost_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacationpost',
            name='title',
            field=models.CharField(default='Trip to <django.db.models.query_utils.DeferredAttribute object at 0x0000020E0B41EC40>, <django.db.models.query_utils.DeferredAttribute object at 0x0000020E0B4118E0>', max_length=128),
        ),
    ]
