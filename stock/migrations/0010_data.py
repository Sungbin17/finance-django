# Generated by Django 2.0.1 on 2018-01-31 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0009_auto_20180131_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('field1', models.TextField(blank=True, null=True)),
                ('field2', models.TextField(blank=True, null=True)),
                ('field3', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'data',
                'managed': False,
            },
        ),
    ]