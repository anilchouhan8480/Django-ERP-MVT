# Generated by Django 3.2.13 on 2022-06-30 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tally_master', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tallymodel',
            name='Transection_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
