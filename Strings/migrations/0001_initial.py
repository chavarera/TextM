# Generated by Django 3.0.2 on 2020-02-25 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('ex_id', models.AutoField(primary_key=True, serialize=False)),
                ('syntax', models.CharField(max_length=1000)),
                ('example', models.CharField(max_length=2000)),
                ('inputs', models.CharField(max_length=3000)),
                ('output', models.CharField(max_length=5000)),
            ],
        ),
    ]
