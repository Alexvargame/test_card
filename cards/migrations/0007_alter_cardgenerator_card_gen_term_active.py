# Generated by Django 4.1.1 on 2022-12-24 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0006_cardgenerator_alter_cardoperation_contr_agent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardgenerator',
            name='card_gen_term_active',
            field=models.CharField(choices=[('1', '1'), ('6', '6'), ('12', '12')], max_length=5),
        ),
    ]