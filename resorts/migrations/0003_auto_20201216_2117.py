# Generated by Django 3.1.2 on 2020-12-16 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resorts', '0002_auto_20201216_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resort',
            name='name',
            field=models.TextField(max_length=120),
        ),
    ]
