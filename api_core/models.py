from django.db import models

# Create your models here.
class medicines(models.Model):
    medicine_name = models.CharField(max_length=50)
    medicine_genre = models.CharField(max_length=50)
    medicine_text = models.TextField()
    medicine_image_url = models.CharField(max_length=500)
    medicine_buy_link = models.CharField(max_length=500)

    def __str__(self):
        return self.medicine_name
