# Generated by Django 3.2.6 on 2021-09-01 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_role'),
        ('post', '0007_alter_postmodel_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='author',
            field=models.ForeignKey(null='Anon', on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
