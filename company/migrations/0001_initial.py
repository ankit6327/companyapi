# Generated by Django 2.1.5 on 2019-02-09 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=100, null='False')),
                ('companyAddress', models.CharField(max_length=255)),
            ],
        ),
    ]