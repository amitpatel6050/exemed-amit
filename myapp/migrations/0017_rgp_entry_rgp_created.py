# Generated by Django 4.0.4 on 2023-03-23 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_rgp_entry_approve_status_rgp_entry_approver_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rgp_entry',
            name='rgp_created',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.user_rgp'),
        ),
    ]
