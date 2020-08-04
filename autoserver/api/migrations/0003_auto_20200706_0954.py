# Generated by Django 3.0.6 on 2020-07-06 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200706_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='业务线')),
            ],
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='机房')),
                ('floor', models.IntegerField(default=1, verbose_name='楼层')),
            ],
        ),
        migrations.AddField(
            model_name='server',
            name='cabinet_num',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='机柜号'),
        ),
        migrations.AddField(
            model_name='server',
            name='cabinet_order',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='机柜中序号'),
        ),
        migrations.AddField(
            model_name='server',
            name='bussiness_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.BusinessUnit', verbose_name='业务线'),
        ),
        migrations.AddField(
            model_name='server',
            name='idc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.IDC', verbose_name='机房'),
        ),
    ]
