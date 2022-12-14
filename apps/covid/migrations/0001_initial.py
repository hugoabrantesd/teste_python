# Generated by Django 4.1.3 on 2022-11-19 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Endereco",
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
                ("cep", models.CharField(max_length=9)),
                ("logradouro", models.CharField(max_length=255)),
                ("complemento", models.CharField(max_length=255)),
                ("bairro", models.CharField(max_length=255)),
                ("localidade", models.CharField(max_length=255)),
                ("uf", models.CharField(max_length=2)),
                ("ibge", models.CharField(max_length=20)),
                ("gia", models.CharField(max_length=20)),
                ("ddd", models.CharField(max_length=2)),
                ("siafi", models.CharField(max_length=20)),
            ],
        ),
    ]
