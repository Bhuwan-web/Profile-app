# Generated by Django 3.2.6 on 2021-09-01 12:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_postmodel_posted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='posted_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]