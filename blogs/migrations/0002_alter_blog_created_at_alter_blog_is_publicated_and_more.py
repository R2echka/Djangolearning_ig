# Generated by Django 5.1.3 on 2024-12-21 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="created_at",
            field=models.DateField(
                blank=True, default=None, null=True, verbose_name="Дата создания"
            ),
        ),
        migrations.AlterField(
            model_name="blog",
            name="is_publicated",
            field=models.BooleanField(default=True, verbose_name="Признак публикации"),
        ),
        migrations.AlterField(
            model_name="blog",
            name="views",
            field=models.IntegerField(default=0, verbose_name="Количество просмотров"),
        ),
    ]
