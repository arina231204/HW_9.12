# Generated by Django 3.2 on 2022-12-09 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_passport_position'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passport',
            old_name='position',
            new_name='employee',
        ),
    ]