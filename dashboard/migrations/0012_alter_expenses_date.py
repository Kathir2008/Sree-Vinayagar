# Generated by Django 4.0.1 on 2022-05-14 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_alter_expenses_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
