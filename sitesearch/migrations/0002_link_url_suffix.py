# Generated by Django 5.1.2 on 2024-10-24 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesearch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='url_suffix',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
