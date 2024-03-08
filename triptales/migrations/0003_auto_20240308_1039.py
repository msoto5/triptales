# Generated by Django 2.2.28 on 2024-03-08 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triptales', '0002_auto_20240307_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='climate',
            field=models.CharField(choices=[('Hot', 'Hot'), ('Cold', 'Cold'), ('Mixed', 'Mixed')], default='', max_length=128),
        ),
        migrations.AddField(
            model_name='location',
            name='setting',
            field=models.CharField(choices=[('City', 'City'), ('Beach', 'Beach'), ('Mountains', 'Mountains'), ('Countryside', 'Countryside')], default='', max_length=128),
        ),
        migrations.AddField(
            model_name='location',
            name='travelPartners',
            field=models.CharField(choices=[('Family', 'Family'), ('Friends', 'Friends'), ('Partner', 'Partner'), ('Solo', 'Solo')], default='', max_length=128),
        ),
        migrations.AddField(
            model_name='location',
            name='vibe',
            field=models.CharField(choices=[('Party', 'Party'), ('Adventure', 'Adventure'), ('Romantic', 'Romantic'), ('Relaxed', 'Relaxed')], default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='country',
            name='continent',
            field=models.CharField(choices=[('Europe', 'Europe'), ('Asia', 'Asia'), ('South America', 'South America'), ('North America', 'North America'), ('Africa', 'Africa'), ('Oceania', 'Oceania')], max_length=10),
        ),
    ]
