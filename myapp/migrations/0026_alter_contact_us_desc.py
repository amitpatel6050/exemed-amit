# Generated by Django 4.1.1 on 2023-07-17 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_us',
            name='Desc',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
