# Generated by Django 5.0.3 on 2024-08-17 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Holder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gmail', models.EmailField(max_length=50)),
                ('paswrd', models.TextField(max_length=20)),
                ('st1', models.CharField(blank=True, max_length=30, null=True)),
                ('st2', models.CharField(blank=True, max_length=30, null=True)),
                ('st3', models.CharField(blank=True, max_length=30, null=True)),
                ('st4', models.CharField(blank=True, max_length=30, null=True)),
                ('st5', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
