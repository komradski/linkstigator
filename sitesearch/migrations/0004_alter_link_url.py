# Generated by Django 4.2.16 on 2024-10-26 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesearch', '0003_alter_link_url_suffix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]