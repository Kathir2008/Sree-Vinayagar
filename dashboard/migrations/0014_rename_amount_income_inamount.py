# Generated by Django 4.0.1 on 2022-05-20 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_income'),
    ]

    operations = [
        migrations.RenameField(
            model_name='income',
            old_name='amount',
            new_name='INamount',
        ),
    ]
