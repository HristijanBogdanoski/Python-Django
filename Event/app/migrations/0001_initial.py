# Generated by Django 5.0.6 on 2024-06-07 19:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('Number_of_events', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('poster', models.ImageField(upload_to='media/')),
                ('isOpen', models.BooleanField(default=False)),
                ('band', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.band')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BandEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.band')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.event')),
            ],
        ),
    ]
