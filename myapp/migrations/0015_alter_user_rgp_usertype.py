# Generated by Django 4.0.4 on 2023-03-19 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_delete_log_delete_petty_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_rgp',
            name='usertype',
            field=models.CharField(choices=[('operator', 'operator'), ('manager', 'manager'), ('approver', 'approver'), ('verifier', 'verifier')], max_length=100),
        ),
    ]
