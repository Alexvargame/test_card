# Generated by Django 4.1.1 on 2022-12-26 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0008_alter_card_card_number_alter_card_card_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='card_termin',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_number',
            field=models.CharField(choices=[('00000000000000', '00000000000000'), ('00000000000000', '00000000000000'), ('00000000000000', '00000000000000'), ('00000000000000', '00000000000000'), ('00000000000000', '00000000000000'), ('00000000000000', '00000000000000'), ('7935355853795645', '7935355853795645'), ('9081709467337062', '9081709467337062'), ('7715570979584960', '7715570979584960'), ('0000000000000000', '0000000000000000'), ('0000000000000000', '0000000000000000'), ('0000000000000000', '0000000000000000'), ('0', '0'), ('0', '0'), ('0000000000000000000', '0000000000000000000'), ('0000000000000000', '0000000000000000'), ('1122653635812414', '1122653635812414')], max_length=22),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_serial',
            field=models.CharField(choices=[('AABB', 'AABB'), ('ABCC', 'ABCC'), ('ACAB', 'ACAB'), ('ADBC', 'ADBC')], max_length=10),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_status',
            field=models.CharField(default='not_active', max_length=15),
        ),
        migrations.AlterField(
            model_name='cardgenerator',
            name='card_gen_serial',
            field=models.CharField(choices=[('AABB', 'AABB'), ('ABCC', 'ABCC'), ('ACAB', 'ACAB'), ('ADBC', 'ADBC')], max_length=10),
        ),
        migrations.AlterField(
            model_name='cardsearch',
            name='card_serial',
            field=models.CharField(blank=True, choices=[('AABB', 'AABB'), ('ABCC', 'ABCC'), ('ACAB', 'ACAB'), ('ADBC', 'ADBC')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='contragent',
            name='contr_agent_serial',
            field=models.CharField(choices=[('AABB', 'AABB'), ('ABCC', 'ABCC'), ('ACAB', 'ACAB'), ('ADBC', 'ADBC')], max_length=10),
        ),
    ]
