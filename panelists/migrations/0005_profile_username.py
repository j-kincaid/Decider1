# Generated by Django 4.1.3 on 2023-01-16 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("panelists", "0004_profile_social_insta_profile_social_other_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="username",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
