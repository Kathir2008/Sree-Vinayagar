# Generated by Django 3.1.4 on 2022-05-11 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20220511_1059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='marraigedate',
            new_name='marriagedate',
        ),
    ]
