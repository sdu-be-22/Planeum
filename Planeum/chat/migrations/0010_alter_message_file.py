# Generated by Django 4.0.3 on 2022-04-12 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_alter_message_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='file',
            field=models.ImageField(blank=True, upload_to='./'),
        ),
    ]
