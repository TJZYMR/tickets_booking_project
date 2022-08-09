# Generated by Django 4.0.6 on 2022-08-09 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_booking_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cinemahallseat',
            name='show_timing',
        ),
        migrations.RemoveField(
            model_name='showtiming',
            name='id',
        ),
        migrations.AddField(
            model_name='showtiming',
            name='seat_no',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Movie_booking_app.cinemahallseat'),
        ),
    ]
