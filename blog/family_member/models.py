from django.db import models

class Family_member(models.Model):
    SEX = (
        ('M', 'Hombre'),
        ('F', 'Mujer'),
    )
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.CharField(max_length=40)
    sex = models.CharField(max_length=1, choices=SEX)
    profession = models.CharField(max_length=40)
    height = models.CharField(max_length=40)

    def __str__(self):
        return f"- ({self.name} | {self.last_name} | edad: {self.age} | sexo:{self.sex} | profesion: {self.profession} | {self.height}"
