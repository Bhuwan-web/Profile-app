# Generated by Django 3.2.6 on 2021-08-30 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0004_alter_profiledecorator_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='userProfile.addressmodel'),
        ),
    ]
