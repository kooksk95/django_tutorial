# Generated by Django 2.0.13 on 2020-11-03 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default='a'),
            preserve_default=False,
        ),
    ]
