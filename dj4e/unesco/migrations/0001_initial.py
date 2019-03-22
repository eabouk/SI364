# Generated by Django 2.1.7 on 2019-03-18 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('justification', models.CharField(max_length=128)),
                ('iso', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Iso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('latitude', models.FloatField(max_length=128)),
                ('longitude', models.FloatField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('year', models.IntegerField(null=True)),
                ('area_hectares', models.FloatField(max_length=128)),
                ('iso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unesco.Category')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unesco.Region')),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unesco.Region')),
            ],
        ),
        migrations.AddField(
            model_name='site',
            name='states',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unesco.States'),
        ),
    ]