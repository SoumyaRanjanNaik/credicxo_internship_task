# Generated by Django 3.0.7 on 2020-07-01 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifsc', models.CharField(max_length=15)),
                ('bank_id', models.CharField(max_length=5)),
                ('branch', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('bank_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Bank',
                'verbose_name_plural': 'Banks',
            },
        ),
    ]
