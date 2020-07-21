# Generated by Django 2.1.7 on 2019-03-06 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("leads", "0006_auto_20190218_1217"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lead",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("assigned", "Assigned"),
                    ("in process", "In Process"),
                    ("converted", "Converted"),
                    ("recycled", "Recycled"),
                    ("closed", "Closed"),
                ],
                max_length=255,
                null=True,
                verbose_name="Status of Lead",
            ),
        ),
    ]
