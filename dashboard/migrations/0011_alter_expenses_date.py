# Generated by Django 4.0.1 on 2022-05-14 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_alter_expenses_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
