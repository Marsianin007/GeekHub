# Generated by Django 4.0.1 on 2022-02-01 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('news', 'newstories'), ('job', 'jobstories'), ('show', 'showstories'), ('ask', 'askstories')], default='news', max_length=20)),
            ],
        ),
    ]
