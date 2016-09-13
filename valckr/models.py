from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CATEGORIA(models.Model):
  IDcategoria= models.IntergerField()
  Nombre= models.CharField(max_length= 30) 

  
 
class SUBCATEGORIA(models.Model)
  IDsubcategoria= models.IntergerField()
  Nombre= models.IntergerField()
  Tags= models.CharField(max_length=50)
  IDcategoria=models.IntergerField()
  

class FOTO(models.Model)
  IDfoto=models.IntergerField()
  Owner= models.CharField(max_length=30)
  secret=models.CharField(max_length=30)
  farm=models.IntergerField()
  titulo=models.CharField(max_length=60)
  ispublic= models.IntergerField()
  isfriend= models.IntergerField()
  isfamily= models.IntergerField()
  dateupload== models.IntergerField()
  Tags=models.CharField(max_length=50)
  URL= models.CharField(max_length=150)
  height= models.IntergerField()
  width= models.IntergerField()
  IDsubcategoria= models.IntergerField()
  
  





