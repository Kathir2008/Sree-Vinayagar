# Generated by Django 4.0.1 on 2022-05-21 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_rename_inamount_income_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Income', models.IntegerField()),
                ('Expense', models.IntegerField()),
                ('Balance', models.IntegerField()),
            ],
        ),
    ]
