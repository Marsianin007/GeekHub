# Generated by Django 4.0.1 on 2022-02-01 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_parse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaveModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='category',
            field=models.CharField(choices=[('newstories', 'newstories'), ('jobstories', 'jobstories'), ('showstories', 'showstories'), ('askstories', 'askstories')], default='news', max_length=20),
        ),
    ]