# Generated by Django 3.2 on 2022-12-09 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passport',
            name='position',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
        ),
    ]