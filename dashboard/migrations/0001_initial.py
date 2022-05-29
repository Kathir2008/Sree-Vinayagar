# Generated by Django 3.1.4 on 2022-05-11 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True, unique=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('district', models.CharField(max_length=200, null=True)),
                ('dob', models.DateTimeField(null=True)),
                ('maritalstatus', models.DateTimeField(null=True)),
                ('marraigedate', models.DateTimeField(null=True)),
                ('user_image', models.ImageField(default='../static/img/avatars/noprofile.png', null=True, upload_to='images/user_images/%Y')),
                ('status', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Users',
                'ordering': ['id'],
                'default_permissions': (),
            },
        ),
    ]