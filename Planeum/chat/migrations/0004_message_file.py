# Generated by Django 4.0.3 on 2022-04-10 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_rename_chat_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='file',
            field=models.FileField(default='', upload_to='document/'),
            preserve_default=False,
        ),
    ]