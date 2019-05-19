from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    código = models.CharField(max_length=6)
    sección = models.PositiveSmallIntegerField()
    año = models.PositiveSmallIntegerField()
    semestre = models.CharField(max_length=9) #Otoño o Primavera
    
    def get_name(self):
        return str(self.nombre)
    
    def get_code(self):
        return str(self.código)
    
    def get_section(self):
        return str(self.sección)
    
    def get_year(self):
        return str(self.año)

    def get_semester(self):
        return str(self.semestre)

    def get_date(self):
        return str(self.get_semester() +" "+self.get_year())

    def __str__(self):
        return str(self.get_code() + "-" + self.get_section())


class Grupo(models.Model):
    nombre = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)


class Alumno(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)