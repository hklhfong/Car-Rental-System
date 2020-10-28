# Generated by Django 2.1.1 on 2018-10-25 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('car_id', models.IntegerField(primary_key=True, serialize=False)),
                ('brand_name', models.CharField(max_length=30)),
                ('transmission', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=30)),
                ('luggage_size', models.CharField(max_length=10)),
                ('seat_number', models.CharField(max_length=10)),
                ('release_year', models.CharField(max_length=10)),
                ('total_rent_january', models.CharField(max_length=4)),
                ('total_rent_february', models.CharField(max_length=4)),
                ('total_rent_march', models.CharField(max_length=4)),
                ('total_rent_april', models.CharField(max_length=4)),
                ('total_rent_may', models.CharField(max_length=4)),
                ('total_rent_june', models.CharField(max_length=4)),
                ('total_rent_july', models.CharField(max_length=4)),
                ('total_rent_august', models.CharField(max_length=4)),
                ('total_rent_september', models.CharField(max_length=4)),
                ('total_rent_october', models.CharField(max_length=4)),
                ('total_rent_november', models.CharField(max_length=4)),
                ('total_rent_december', models.CharField(max_length=4)),
            ],
        ),
    ]