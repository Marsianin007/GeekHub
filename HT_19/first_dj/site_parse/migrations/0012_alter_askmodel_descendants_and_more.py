# Generated by Django 4.0.1 on 2022-02-04 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_parse', '0011_remove_askmodel_url_remove_jobmodel_descendants_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='askmodel',
            name='descendants',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='descendants',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='showmodel',
            name='descendants',
            field=models.CharField(max_length=200),
        ),
    ]
