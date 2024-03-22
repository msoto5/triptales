# Generated by Django 2.1.5 on 2024-03-22 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triptales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='country',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='location',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='vacationpost',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='vacationpost',
            name='title',
            field=models.CharField(default='Trip to <django.db.models.query_utils.DeferredAttribute object at 0x00000163DFF09550>, <django.db.models.query_utils.DeferredAttribute object at 0x00000163DFF129A0>', max_length=128),
        ),
    ]
