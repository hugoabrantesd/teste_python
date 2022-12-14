# Generated by Django 4.1.3 on 2022-12-09 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("covid", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Covid",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("uid", models.IntegerField()),
                ("uf", models.CharField(max_length=2)),
                ("state", models.CharField(max_length=20)),
                ("cases", models.IntegerField()),
                ("deaths", models.IntegerField()),
                ("suspects", models.IntegerField()),
                ("refuses", models.IntegerField()),
                ("datetime", models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name="Endereco",
        ),
    ]
