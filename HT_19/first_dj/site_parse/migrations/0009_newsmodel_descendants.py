# Generated by Django 4.0.1 on 2022-02-04 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_parse', '0008_jobmodel_newsmodel_showmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsmodel',
            name='descendants',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
    ]