from django.db import models
from django.core.validators import MaxLengthValidator
from test.test_imageop import MAX_LEN


class Departamento(models.Model):
    nomDepartamento      = models.CharField(max_length=15)
    jefe                 = models.CharField(max_length=15)
    idEstadoDepartamneto = models.IntegerField()
    eliminado            = models.BooleanField(default=False)
   
    def __str__(self):
        return self.nomDepartamento


class Cliente(models.Model):
    identificacion       = models.CharField(max_length=15)
    idTipoId             = models.IntegerField()
    nombres              = models.CharField(max_length=100, blank=True)
    apellidos            = models.CharField(max_length=100, blank=True)
    email                = models.EmailField(max_length=100, blank=True)
    direccion            = models.CharField(max_length=100, blank=True)
    idEstadoCliente      = models.IntegerField()
    telefonos            = models.CharField(max_length=100, blank=True)
    eliminado            = models.BooleanField(default=False)
    departamento         = models.ForeignKey('Departamento')
    
    
    def __str__(self):
        if self.nombres <>'' and self.apellidos <>'':
            return "%s %s"  % (self.nombres,self.apellidos)

class PersonalSoporte(models.Model):
    identificacion       = models.CharField(max_length=15)
    nombres              = models.CharField(max_length=100, blank=True)
    apellidos            = models.CharField(max_length=100, blank=True)
    email                = models.EmailField(max_length=100, blank=True)
    direccion            = models.CharField(max_length=100, blank=True)
    idEstadoSoporte      = models.IntegerField()
    telefonos            = models.CharField(max_length=100, blank=True)
    idRol                = models.IntegerField()
    eliminado            = models.BooleanField(default=False)  

    def __str__(self):
        if self.nombres <>'' and self.apellidos <>'':
            return "%s %s"  % (self.nombres,self.apellidos)

class Ticket(models.Model):
    idDescripcion        = models.IntegerField()
    fechaReportado       = models.DateField(auto_now_add = True)
    fechaArreglado       = models.DateField(auto_now_add = True)
    cliente              = models.ForeignKey('Cliente')
    idEstadoTicket       = models.IntegerField()
    eliminado            = models.BooleanField(default=False)  

    def __str__(self):
        return self.idEstadoTicket.valor

class Parametro(models.Model):
    atributo        =models.CharField(max_length=50)
    descripcion      =models.CharField(max_length=200)
    estadoParametro =models.CharField(max_length=1)
 
    def __str__(self):
        return self.atributo


class ValorParametro(models.Model):    
    valor                =models.CharField(max_length=30)
    parametro            = models.ForeignKey('Parametro')
    orden                =models.CharField(max_length=3)
    estadoValorParametro =models.CharField(max_length=1)
    

    def __str__(self):
        return self.valor