# Generated by Django 4.1.1 on 2023-01-06 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0009_card_card_termin_alter_card_card_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ammount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ammount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CardDateActiveSearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_date_end_active', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CardDateCreateSearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_date_create', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='card',
            name='card_number',
            field=models.CharField(blank=True, choices=[('00000000000000', '00000000000000'), ('00000000000000', '00000000000000'), ('00000000000000', '00000000000000'), ('00000000000000', '00000000000000'), ('00000000000000', '00000000000000'), ('00000000000000', '00000000000000'), ('7935355853795645', '7935355853795645'), ('9081709467337062', '9081709467337062'), ('7715570979584960', '7715570979584960'), ('0000000000000000', '0000000000000000'), ('0000000000000000', '0000000000000000'), ('0000000000000000', '0000000000000000'), ('0', '0'), ('0', '0'), ('0000000000000000000', '0000000000000000000'), ('0000000000000000', '0000000000000000'), ('1122653635812414', '1122653635812414'), ('1122481446777814', '1122481446777814'), ('1122632882138576', '1122632882138576'), ('1122278633025710', '1122278633025710'), ('1122819770338980', '1122819770338980'), ('1122247018022889', '1122247018022889'), ('1122426442083563', '1122426442083563'), ('1122822108068111', '1122822108068111'), ('1122762433301189', '1122762433301189'), ('1122763877202897', '1122763877202897'), ('1122846897724220', '1122846897724220'), ('0000000000000000', '0000000000000000'), ('1423135027554089', '1423135027554089'), ('1423724519384112', '1423724519384112'), ('1423829376801004', '1423829376801004'), ('1423777076664299', '1423777076664299'), ('1312703579504353', '1312703579504353'), ('1312703579504353', '1312703579504353'), ('1312703579504353', '1312703579504353'), ('1312703579504353', '1312703579504353'), ('1312508191999674', '1312508191999674'), ('1312229442491741', '1312229442491741'), ('1312549349782817', '1312549349782817'), ('1312775361043014', '1312775361043014'), ('1312760223685691', '1312760223685691'), ('1312169822274147', '1312169822274147'), ('1312281440903985', '1312281440903985'), ('1312800797195448', '1312800797195448'), ('1312293335805094', '1312293335805094'), ('1312635237029000', '1312635237029000'), ('1312633324167482', '1312633324167482'), ('1312439566794286', '1312439566794286'), ('1233473932680431', '1233473932680431'), ('1233969395400020', '1233969395400020'), ('1122479407363034', '1122479407363034'), ('1122651263530038', '1122651263530038'), ('1122385703937468', '1122385703937468'), ('1122607858032732', '1122607858032732'), ('1122208253402235', '1122208253402235'), ('1122109511941065', '1122109511941065')], max_length=22),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_termin',
            field=models.CharField(blank=True, choices=[('1', '1'), ('6', '6'), ('12', '12')], max_length=5, null=True),
        ),
    ]
