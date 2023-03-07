# Generated by Django 4.1.3 on 2023-01-17 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("panelists", "0006_alter_profile_brief_bio"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="profle_image",
        ),
        migrations.AddField(
            model_name="profile",
            name="profile_image",
            field=models.ImageField(
                blank=True,
                default="profiles/default-profile.png",
                null=True,
                upload_to="profiles/",
            ),
        ),
    ]
