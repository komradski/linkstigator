# Generated by Django 4.2.16 on 2024-10-26 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modeltest', '0009_rename_lang_language_language'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='organizationlanguage',
            unique_together={('organization', 'language')},
        ),
    ]
