from django.db import models


class QuoteText(models.Model):
    description = models.TextField(max_length=1024)
    author = models.CharField(max_length=124)

    def __str__(self):
        return self.author
