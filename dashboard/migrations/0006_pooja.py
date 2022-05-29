# Generated by Django 3.1.4 on 2022-05-11 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20220511_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pooja',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, null=True)),
                ('desc', models.CharField(max_length=200, null=True)),
                ('amount', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Pooja',
                'ordering': ['id'],
                'default_permissions': (),
            },
        ),
    ]