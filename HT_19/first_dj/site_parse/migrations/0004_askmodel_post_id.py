# Generated by Django 4.0.1 on 2022-02-03 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_parse', '0003_rename_savemodel_askmodel_alter_mymodel_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='askmodel',
            name='post_id',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
