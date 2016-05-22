from django.db import models

# Create your models here.

    
class Character(models.Model):
    Mighty = 'Mighty squire'
    Power = 'Power squire'
    Competent = 'Competent Squire'
    Igor = 'Igor'
    role = (
        (Mighty,'Mighty squire'),
        (Power,'Power squire'),
        (Competent,'Competent Squire'),
        (Igor,'Igor'),
        )
    
    role = models.CharField(max_length=16,
                            choices=role,
                            default=Mighty)
    
    power = models.IntegerField(default=1)
    speed = models.IntegerField(default=2)
    capacity_width = models.IntegerField(default=4)
    capacity_height = models.IntegerField(default=4)
    
    class Meta:
        verbose_name_plural = "Characters"

    def __str__(self):
        return self.role
