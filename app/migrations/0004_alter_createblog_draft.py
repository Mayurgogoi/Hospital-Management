# Generated by Django 3.2.8 on 2021-10-20 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_createblog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createblog',
            name='Draft',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
