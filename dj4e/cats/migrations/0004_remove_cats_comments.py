# Generated by Django 2.1.7 on 2019-02-26 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0003_cats_foods'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cats',
            name='comments',
        ),
    ]