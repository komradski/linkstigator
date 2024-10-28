# Generated by Django 4.2.16 on 2024-10-28 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modeltest', '0011_organization_country_alter_link_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('response', models.JSONField(null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ('organization', 'url')},
        ),
        migrations.AlterModelOptions(
            name='organization',
            options={'ordering': ('name', 'type')},
        ),
        migrations.CreateModel(
            name='ArticleLinkMeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=255)),
                ('articlelink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modeltest.articlelink')),
            ],
        ),
    ]