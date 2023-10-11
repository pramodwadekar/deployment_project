# Generated by Django 4.2.6 on 2023-10-10 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullname', models.CharField(max_length=50)),
                ('DOB', models.DateField()),
                ('Email', models.EmailField(max_length=50)),
                ('Contact', models.BigIntegerField()),
                ('Gender', models.CharField(max_length=50)),
                ('Country', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('Pincode', models.CharField(max_length=50)),
                ('Qualification', models.CharField(max_length=50)),
            ],
        ),
    ]
