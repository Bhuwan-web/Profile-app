# Generated by Django 3.2.6 on 2021-09-01 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_role'),
        ('post', '0003_alter_postmodel_posted_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='author',
        ),
        migrations.AddField(
            model_name='postmodel',
            name='author',
            field=models.ManyToManyField(default='Anon', to='users.User'),
        ),
    ]
