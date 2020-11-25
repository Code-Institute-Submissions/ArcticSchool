from django.db import models

# Create your models here.


class Levels(models.Model):
    class levelChoices(models.TextChoices):
        Level_1 = '1',
        Level_2 = '2',
        Level_3 = '3',
        Level_4 = '4'

    title = models.TextField(max_length=40)
    level = models.CharField(choices=levelChoices.choices,
                             default=levelChoices.Level_1, max_length=1)
    description = models.TextField(max_length=130)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.TextField(max_length=40)
    description = models.TextField(max_length=130)

    def __str__(self):
        return self.title


class Social(models.Model):
    class levelChoices(models.TextChoices):
        Facebook = 'fa-facebook-f',
        YouTube = 'fa-youtube',
        Pintereset = 'fa-pintereset-p',
        Snapchat = 'fa-snapchat-ghost',
        Twitter = 'fa-twitter',
        Instagram = 'fa-instagram',
        TikTok = 'fa-tiktok',
        Vimeo = 'fa-viemo-v'

    title = models.TextField(max_length=40)
    icon = models.CharField(choices=levelChoices.choices,max_length=30)
    url = models.URLField(max_length=1024, default='#', null=True, blank=True)

    def __str__(self):
        return self.title
