# Generated by Django 4.1.12 on 2023-10-15 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=128)),
                ('email', models.EmailField(default=None, max_length=254, unique=True)),
                ('password', models.CharField(default=None, max_length=128)),
            ],
            options={
                'db_table': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('trip_id', models.AutoField(primary_key=True, serialize=False)),
                ('trip_name', models.CharField(default='Default Trip Name', max_length=100)),
                ('email', models.EmailField(default='example@example.com', max_length=254)),
                ('trip_from', models.CharField(default='Default From', max_length=100)),
                ('trip_to', models.CharField(default='Default To', max_length=100)),
                ('start_date', models.DateField(default=None)),
                ('return_date', models.DateField(default=None)),
                ('num_days', models.IntegerField(default=1)),
                ('accommodation_per_trip', models.DecimalField(decimal_places=2, default=1000.0, max_digits=10)),
                ('num_trip_mates', models.PositiveIntegerField(default=5)),
                ('trip_description', models.TextField(default='Default Trip Description')),
            ],
            options={
                'db_table': 'Trips',
            },
        ),
        migrations.CreateModel(
            name='TripPhotos',
            fields=[
                ('trip_image_id', models.AutoField(primary_key=True, serialize=False)),
                ('trip_image', models.ImageField(default='default_image.jpg', upload_to='trip_images/')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.trip')),
            ],
            options={
                'db_table': 'Trip_images',
            },
        ),
    ]
