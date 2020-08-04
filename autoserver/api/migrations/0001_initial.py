# Generated by Django 3.0.6 on 2020-07-05 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=32, verbose_name='主机名')),
                ('last_date', models.DateField(blank=True, null=True, verbose_name='最近汇报时间')),
            ],
        ),
    ]
