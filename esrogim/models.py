from django.db import models

class Esrog(models.Model):
    size = models.IntegerField()
    clarity = models.IntegerField()
    odor_strength = models.IntegerField(default=0)
    texture_smoothness = models.IntegerField(default=0)
    ripeness_score = models.IntegerField(default=0)
    image_url = models.URLField(max_length=500, default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSAd1g0lcUsdJbWuqcmOp6G8hD4A92kszSVeLFP476S_baPJWzFDSwxAbjDvHhcZ6LQ998&usqp=CAU")
    video_url = models.URLField(max_length=500, default="https://www.youtube.com/embed/t10Ajcd_G-w")
    estimated_price = models.IntegerField(default=0)
    reserved = models.CharField(max_length=100, default='')

    def calculate_price(self):
        size_weight = 0.1
        clarity_weight = 0.15
        odor_weight = 0.2
        texture_weight = 0.15
        ripeness_weight = 0.2

        estimated_price = (
                       self.size_score * size_weight +
                       self.clarity_score * clarity_weight +
                       self.odor_strength * odor_weight +
                       self.texture_smoothness * texture_weight +
                       self.ripeness_score * ripeness_weight)

    def __str__(self):
        return f"Esrog: Size - {self.size}, estimated_price - {self.estimated_price}"
