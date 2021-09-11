# Generated by Django 3.2.7 on 2021-09-11 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_hospital'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=3)),
                ('sex', models.CharField(max_length=10)),
                ('sexa', models.IntegerField(choices=[(1, 'ชาย'), (2, 'หญิง')])),
            ],
            options={
                'verbose_name': 'patient',
                'verbose_name_plural': 'patients',
            },
        ),
        migrations.AlterField(
            model_name='doctor',
            name='skill',
            field=models.IntegerField(choices=[(1, 'ระดับปฏิบัติการ'), (2, 'ระดับชำนาญการ'), (3, 'ระดับชำนาญการพิเศษ'), (4, 'ระดับเชี่ยวชาญ')]),
        ),
    ]
