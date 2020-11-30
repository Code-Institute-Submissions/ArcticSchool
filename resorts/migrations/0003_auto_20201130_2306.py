# Generated by Django 3.1.2 on 2020-11-30 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resorts', '0002_remove_resort_street_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resort',
            name='styles',
        ),
        migrations.AddField(
            model_name='resort',
            name='bottom_altitude',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='resort',
            name='open_season',
            field=models.CharField(default='December - April', max_length=120),
        ),
        migrations.AddField(
            model_name='resort',
            name='resort_altitude',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='resort',
            name='top_altitude',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='resort',
            name='about',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='resort',
            name='levels',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='resort',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]
