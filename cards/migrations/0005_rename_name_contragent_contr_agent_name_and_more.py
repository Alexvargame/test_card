# Generated by Django 4.1.1 on 2022-12-23 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_cardoperation_contragent_alter_card_card_serial_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contragent',
            old_name='name',
            new_name='contr_agent_name',
        ),
        migrations.AddField(
            model_name='contragent',
            name='contr_agent_number',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contragent',
            name='contr_agent_serial',
            field=models.CharField(choices=[('AAB', 'AAB'), ('ACC', 'ACC'), ('CAB', 'CAB'), ('ABC', 'ABC')], default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cardoperation',
            name='contr_agent',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B')], max_length=20),
        ),
    ]