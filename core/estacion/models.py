from django.db import models

# Create your models here.
class Station(models.Model):
    name = models.CharField(max_length = 255)    
    location = models.CharField(max_length = 1000)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Station'
        verbose_name_plural = 'Stations'

        db_table = 'station'



class Equipment(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    equipment_type = models.BooleanField(default = False) # 1 - Internal 2 - External
    physical_id = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)
    brand = models.CharField(max_length = 255)
    model = models.CharField(max_length = 255)
    owner = models.BooleanField(default = False) # 1 - Own equipment 2 - Its not our equipment


    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipments'

        db_table = 'equipment'