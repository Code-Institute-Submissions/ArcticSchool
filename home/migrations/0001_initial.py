# Generated by Django 3.1.2 on 2020-11-29 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LessonCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=40)),
                ('description', models.TextField(max_length=130)),
            ],
        ),
        migrations.CreateModel(
            name='LevelCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=40)),
                ('level', models.CharField(choices=[('1', 'Level 1'), ('2', 'Level 2'), ('3', 'Level 3'), ('4', 'Level 4')], default='1', max_length=1)),
                ('description', models.TextField(max_length=130)),
            ],
        ),
        migrations.CreateModel(
            name='SocialIcon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=40)),
                ('icon', models.CharField(choices=[('fa-facebook-f', 'Facebook'), ('fa-youtube', 'Youtube'), ('fa-pinterest-p', 'Pintereset'), ('fa-snapchat-ghost', 'Snapchat'), ('fa-twitter', 'Twitter'), ('fa-instagram', 'Instagram'), ('fa-tiktok', 'Tiktok'), ('fa-viemo-v', 'Vimeo')], max_length=30)),
                ('url', models.URLField(blank=True, default='', max_length=1024, null=True)),
            ],
        ),
    ]
