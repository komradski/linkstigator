# Generated by Django 4.2.16 on 2024-10-28 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesearch', '0004_alter_link_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='response',
            field=models.JSONField(null=True),
        ),
    ]
