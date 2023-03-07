# Generated by Django 4.1.3 on 2022-12-29 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("panelists", "0002_rename_social_website_profile_website_and_more"),
        ("artworks", "0008_artwork_featured_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="artwork",
            name="critic",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="panelists.profile",
            ),
        ),
    ]
