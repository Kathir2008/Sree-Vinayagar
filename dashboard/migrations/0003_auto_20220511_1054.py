# Generated by Django 3.1.4 on 2022-05-11 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_remove_users_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='maritalstatus',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
