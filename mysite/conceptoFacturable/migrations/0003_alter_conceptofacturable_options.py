# Generated by Django 4.1.2 on 2022-10-24 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conceptoFacturable', '0002_alter_conceptofacturable_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conceptofacturable',
            options={'ordering': ['pk'], 'verbose_name': 'concepto_facturable', 'verbose_name_plural': 'conceptos_facturables'},
        ),
    ]
