# Generated by Django 4.2.6 on 2023-12-04 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lk', '0002_alter_articles_options_alter_articles_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=50, verbose_name='ФИО'),
        ),
    ]
