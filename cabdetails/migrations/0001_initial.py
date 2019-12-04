# Generated by Django 3.0 on 2019-12-04 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CabDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_cab', models.CharField(default='cab', max_length=20)),
                ('pickup', models.CharField(max_length=200)),
                ('destination', models.CharField(max_length=200)),
                ('drop', models.CharField(max_length=200)),
                ('cabname', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=100)),
                ('capacity', models.IntegerField(default=4)),
                ('peak', models.IntegerField()),
                ('mid', models.IntegerField()),
                ('off', models.IntegerField()),
            ],
        ),
    ]