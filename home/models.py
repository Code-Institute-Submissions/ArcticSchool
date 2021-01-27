""" Home App Models """
from django.db import models


class LevelCard(models.Model):
    """ Level Cards Model - for users """
    class LevelChoices(models.TextChoices):
        """ Choices for dropdown list in Level Cards """
        Level_1 = '1'
        Level_2 = '2'
        Level_3 = '3'
        Level_4 = '4'

    title = models.TextField(max_length=40)
    level = models.CharField(choices=LevelChoices.choices,
                             default=LevelChoices.Level_1, max_length=1)
    description = models.TextField(max_length=130)

    def __str__(self):
        return self.title


class LessonCard(models.Model):
    """ Lessons Information Cards Model """
    title = models.TextField(max_length=40)
    description = models.TextField(max_length=130)

    def __str__(self):
        return self.title


class SocialIcon(models.Model):
    """ Social Icons model """
    class LevelChoices(models.TextChoices):
        """ Choices for dropdown list in Social Icons """
        Facebook = 'fa-facebook-f'
        YouTube = 'fa-youtube'
        Pintereset = 'fa-pinterest-p'
        Snapchat = 'fa-snapchat-ghost'
        Twitter = 'fa-twitter'
        Instagram = 'fa-instagram'
        TikTok = 'fa-tiktok'
        Vimeo = 'fa-viemo-v'

    class NameChoices(models.TextChoices):
        """ Choices for dropdown list in Social Icons """
        Facebook = 'facebook'
        YouTube = 'youtube'
        Pintereset = 'pinterest'
        Snapchat = 'snapchat'
        Twitter = 'twitter'
        Instagram = 'instagram'
        TikTok = 'tiktok'
        Vimeo = 'viemo'

    name = models.TextField(choices=NameChoices.choices,
                            max_length=40, null=False, blank=False, default='Facebook')
    icon = models.CharField(choices=LevelChoices.choices, max_length=30)
    url = models.URLField(max_length=1024, default='', null=True, blank=True)

    def __str__(self):
        return self.name
