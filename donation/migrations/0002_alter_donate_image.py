# Generated by Django 3.2.9 on 2021-11-16 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donate',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='donate/'),
        ),
    ]
