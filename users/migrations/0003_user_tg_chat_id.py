# Generated by Django 4.2 on 2025-03-03 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_options_remove_user_username_user_avatar_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="tg_chat_id",
            field=models.CharField(
                blank=True, max_length=30, null=True, verbose_name="id TG-чата"
            ),
        ),
    ]
