# Generated by Django 3.1.2 on 2021-01-29 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210129_0001'),
        ('resorts', '0006_auto_20201216_2122'),
        ('lessons', '0005_remove_category_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='lessons.category'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='home.levelcard'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='participants',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='resort',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='resorts.resort'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
