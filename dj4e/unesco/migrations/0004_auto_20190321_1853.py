# Generated by Django 2.1.7 on 2019-03-21 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0003_site_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='iso',
        ),
        migrations.RemoveField(
            model_name='category',
            name='justification',
        ),
        migrations.RemoveField(
            model_name='region',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='region',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='states',
            name='region',
        ),
        migrations.AddField(
            model_name='site',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unesco.Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='justification',
            field=models.CharField(default='-', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='latitude',
            field=models.FloatField(default=0.0, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='longitude',
            field=models.FloatField(default=0.0, max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='site',
            name='iso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unesco.Iso'),
        ),
    ]
