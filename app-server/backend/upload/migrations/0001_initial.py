# Generated by Django 4.2 on 2023-04-29 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Packagey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pack_name', models.CharField(max_length=64)),
                ('version_field', models.CharField(max_length=9)),
                ('stars', models.IntegerField()),
                ('downloads', models.IntegerField()),
                ('metrics_score', models.FloatField(max_length=4)),
            ],
        ),
    ]
