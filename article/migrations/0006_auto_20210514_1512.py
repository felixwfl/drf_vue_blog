# Generated by Django 3.1.3 on 2021-05-14 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20210514_1122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='title',
            new_name='text',
        ),
    ]