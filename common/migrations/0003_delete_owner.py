# Generated by Django 4.1.2 on 2022-11-09 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_remove_owner_ac_holder_name_remove_owner_ac_number_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Owner',
        ),
    ]
