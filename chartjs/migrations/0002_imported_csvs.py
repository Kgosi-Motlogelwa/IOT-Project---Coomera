# Generated by Django 3.1.7 on 2021-02-23 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartjs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imported_CSVs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100000)),
                ('DateTime', models.DateTimeField()),
                ('Measurement_1', models.FloatField()),
            ],
        ),
    ]
