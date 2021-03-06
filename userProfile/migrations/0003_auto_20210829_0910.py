# Generated by Django 3.2.6 on 2021-08-29 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0002_userprofile_login_infos'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileDecorator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.FileField(upload_to='')),
                ('bio', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='userProfile.profiledecorator'),
        ),
    ]
