# Generated by Django 4.1 on 2022-08-10 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='web',
            field=models.URLField(blank=True, max_length=50),
        ),
    ]
