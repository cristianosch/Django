# Generated by Django 3.2.7 on 2021-10-02 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
