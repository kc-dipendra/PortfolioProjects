# Generated by Django 4.1.7 on 2023-03-27 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Teacher_Name', models.CharField(max_length=50)),
                ('Teacher_Qualification', models.CharField(max_length=50)),
                ('Teacher_Subject', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=50)),
                ('Phone', models.IntegerField()),
            ],
        ),
    ]
