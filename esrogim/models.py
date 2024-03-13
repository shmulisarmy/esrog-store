from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Esrog(models.Model):
    size = models.IntegerField()
    clarity = models.IntegerField()
    odor_strength = models.IntegerField(default=0)
    texture_smoothness = models.IntegerField(default=0)
    ripeness_score = models.IntegerField(default=0)
    image_url = models.URLField(max_length=500, default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSAd1g0lcUsdJbWuqcmOp6G8hD4A92kszSVeLFP476S_baPJWzFDSwxAbjDvHhcZ6LQ998&usqp=CAU")
    video_url = models.URLField(max_length=500, default="https://www.youtube.com/embed/t10Ajcd_G-w")
    estimated_price = models.IntegerField(default=0)
    reserved = models.BooleanField(default=False)

    def __str__(self):
        return f"Esrog: Size - {self.size}, estimated_price - {self.estimated_price}"

@receiver(post_save, sender=Esrog)
def calculate_price(sender, instance, created, *args, **kwargs):
    if instance.estimated_price:
        return
    
    size_weight = 7
    clarity_weight = 12
    odor_weight = 5
    texture_weight = 13
    ripeness_weight = 8

    estimated_price = (
                    instance.size * size_weight +
                    instance.clarity * clarity_weight +
                    instance.odor_strength * odor_weight +
                    instance.texture_smoothness * texture_weight +
                    instance.ripeness_score * ripeness_weight)

    instance.estimated_price = estimated_price
    instance.save()
