# Generated by Django 4.2.6 on 2023-12-29 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_LITRevu_app', '0002_ticket_description_ticket_image_ticket_time_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='title',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]