# Generated by Django 2.2.14 on 2023-05-14 13:27

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20230514_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=django_cryptography.fields.encrypt(models.SlugField()),
        ),
    ]
