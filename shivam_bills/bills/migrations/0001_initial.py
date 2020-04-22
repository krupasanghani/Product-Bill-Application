# Generated by Django 2.1.15 on 2020-04-21 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='BillModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bills.AreaName')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=500)),
                ('unit', models.CharField(choices=[('nos', 'NOS'), ('meter', 'MTRS'), ('feet', 'FEET')], max_length=5)),
                ('prize', models.IntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bills.CompanyBill')),
            ],
        ),
        migrations.AddField(
            model_name='billmodel',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bills.CompanyBill'),
        ),
        migrations.AddField(
            model_name='billmodel',
            name='items',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bills.ProductItem'),
        ),
    ]
