# Generated by Django 4.1.1 on 2022-12-19 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='card_balance',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_begin_active',
            field=models.DateTimeField(blank=True, default='2022-01-01 00:00:00'),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_end_active',
            field=models.DateTimeField(blank=True, default='2030-01-01 00:00:00'),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_number',
            field=models.CharField(max_length=20),
        ),
    ]