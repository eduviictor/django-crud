# Generated by Django 3.2.5 on 2021-07-10 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=30, unique=True)),
                ('name', models.TextField(max_length=30)),
                ('lastName', models.TextField(blank=True, max_length=30, null=True)),
                ('profileImageUrl', models.TextField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, max_length=30, null=True)),
                ('email', models.TextField(unique=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Not Specified')], max_length=13)),
            ],
        ),
    ]
