# Generated by Django 2.2 on 2020-02-26 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number1', models.IntegerField()),
                ('operater', models.CharField(max_length=255)),
                ('number2', models.IntegerField()),
                ('result', models.IntegerField()),
            ],
        ),
    ]
