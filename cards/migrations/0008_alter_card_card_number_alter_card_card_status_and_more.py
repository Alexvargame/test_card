# Generated by Django 4.1.1 on 2022-12-25 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0007_alter_cardgenerator_card_gen_term_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='card_number',
            field=models.CharField(choices=[], max_length=22),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_status',
            field=models.CharField(default='not_acvtive', max_length=15),
        ),
        migrations.AlterField(
            model_name='cardgenerator',
            name='card_gen_number',
            field=models.CharField(max_length=22),
        ),
    ]
