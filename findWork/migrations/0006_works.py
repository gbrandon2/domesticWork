# Generated by Django 2.1.3 on 2018-11-12 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findWork', '0005_auto_20181112_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=30)),
                ('Type', models.CharField(max_length=30)),
                ('StartDate', models.DateField()),
                ('Finaldate', models.DateField()),
                ('Price', models.IntegerField()),
            ],
        ),
    ]
