# Generated by Django 3.1.4 on 2021-01-24 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=255)),
                ('bio', models.CharField(max_length=2083)),
                ('status', models.IntegerField()),
            ],
        ),
    ]