# Generated by Django 5.1.6 on 2025-02-26 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bank_auth", "0004_otp_code"),
    ]

    operations = [
        migrations.CreateModel(
            name="OtpCode",
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
                ("email", models.CharField(max_length=255, null=True)),
                ("otp", models.IntegerField(null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Otp_code",
        ),
    ]
