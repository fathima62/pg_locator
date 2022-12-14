# Generated by Django 4.0.6 on 2022-10-15 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('second_name', models.CharField(max_length=20)),
                ('c_email', models.CharField(max_length=100)),
                ('c_phone', models.BigIntegerField()),
                ('c_address', models.CharField(max_length=300)),
                ('c_password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.BigIntegerField()),
                ('address', models.CharField(max_length=100)),
                ('ac_number', models.BigIntegerField()),
                ('ifsc', models.CharField(max_length=20)),
                ('ac_holder_name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('photo', models.ImageField(default='', upload_to='owner/')),
            ],
        ),
    ]
