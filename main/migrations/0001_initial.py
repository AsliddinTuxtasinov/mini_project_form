# Generated by Django 3.2.3 on 2021-05-27 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titile', models.CharField(max_length=128, verbose_name='title')),
                ('body', models.TextField(verbose_name='content')),
            ],
        ),
    ]
