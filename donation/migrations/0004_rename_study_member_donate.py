# Generated by Django 3.2.9 on 2021-11-20 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0003_auto_20211117_0206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='study',
            new_name='Donate',
        ),
    ]
