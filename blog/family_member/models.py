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
    birth_day = models.DateField()

    def __str__(self):
        return f"- Nombre: {self.name} | Apellido: {self.last_name} | fecha de nacimiento: {self.birth_day} | edad: {self.age} | sexo:{self.sex} | altura: {self.height} | profesion: {self.profession} "
