# Generated by Django 3.2.13 on 2022-06-30 06:54

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('State', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier_models',
            fields=[
                ('Supplier_Code', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=25)),
                ('supplier_prefix', models.CharField(default='SUP0', max_length=20)),
                ('is_del', models.BooleanField(default=False)),
                ('Email', models.EmailField(max_length=254)),
                ('Mobile_NO', models.BigIntegerField()),
                ('GSTIN', models.CharField(blank=True, max_length=25, null=True)),
                ('suppliers_product', models.CharField(blank=True, max_length=25, null=True)),
                ('title', models.CharField(choices=[('MR.', 'MR.'), ('MS.', 'MS.'), ('MRS.', 'MRS.')], default=('MR.', 'MR.'), max_length=25)),
                ('Billing_Name', models.CharField(max_length=50)),
                ('Street_h_n', models.CharField(blank=True, max_length=50, null=True)),
                ('City', models.CharField(blank=True, max_length=50, null=True)),
                ('postalcode', models.IntegerField(blank=True, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('Remark', models.CharField(blank=True, max_length=200, null=True)),
                ('Place_Of_Supply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='State_s', to='State.state_model')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='State.state_model')),
            ],
        ),
    ]
