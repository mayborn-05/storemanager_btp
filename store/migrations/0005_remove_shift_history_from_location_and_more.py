# Generated by Django 4.1.5 on 2023-07-09 14:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0004_ledger_current_department"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="shift_history",
            name="From_Location",
        ),
        migrations.RemoveField(
            model_name="shift_history",
            name="To_Location",
        ),
        migrations.AddField(
            model_name="shift_history",
            name="From",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="shift_history",
            name="To",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
