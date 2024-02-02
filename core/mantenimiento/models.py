from django.db import models
from core.estacion.models import Station

from django.contrib.auth.models import User

# Create your models here.
        
class FormType(models.Model):
    name = models.CharField(max_length=300)
    

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Form Type'
        verbose_name_plural = 'Form Types'
        db_table = 'form_type'


class Maintenance(models.Model):
    station = models.ForeignKey(Station, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    whetter_description = models.TextField()
    consumables = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.station + ' | ' + self.id

    class Meta:
        verbose_name = 'Maintenance'
        verbose_name_plural = 'Maintenance'
        db_table = 'Maintenance'

class Question(models.Model):
    form_type = models.ForeignKey(FormType, on_delete=models.PROTECT)
    question = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.question

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        db_table = 'question'



class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    maintenance = models.ForeignKey(Maintenance, on_delete=models.PROTECT)
    answer = models.BooleanField(default=False)
    observations = models.TextField()
    # Queda pendiente este campo dado que no se si sera unicamente una image o seran multiples imagenes
    # img = models.ImgField() #Necesito instalar pillow


    def __str__(self) -> str:
        return self.answer

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        db_table = 'answer'