# Generated by Django 3.1.2 on 2021-01-22 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20210122_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='receiving_newsletter',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False),
        ),
    ]
