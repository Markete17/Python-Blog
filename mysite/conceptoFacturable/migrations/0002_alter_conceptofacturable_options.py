# Generated by Django 4.1.2 on 2022-10-24 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conceptoFacturable', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conceptofacturable',
            options={'ordering': ['-concepto'], 'verbose_name': 'concepto_facturable', 'verbose_name_plural': 'conceptos_facturables'},
        ),
    ]
