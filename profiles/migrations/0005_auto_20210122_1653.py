# Generated by Django 3.1.2 on 2021-01-22 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20210122_1650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_country',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_county',
            new_name='county',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_first_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_last_name',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_phone_number',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_postcode',
            new_name='postcode',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_street_address1',
            new_name='street_address1',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_street_address2',
            new_name='street_address2',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_town_or_city',
            new_name='town_or_city',
        ),
    ]
