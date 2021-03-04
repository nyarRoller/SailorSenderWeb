from django.db import models

class Theame(models.Model):
    theame_text = models.CharField(max_length=20, help_text="Text of the theame")

    theame_user = models.CharField(max_length = 16, help_text = "Username")

    class Meta:
        ordering = ["-theame_text"]

    # def get_absolute_url(self):
    #      return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.theame_text