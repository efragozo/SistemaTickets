from django.contrib import admin

from aplicacion.models import *

class ClienteAdmin(admin.ModelAdmin):
    list_display=('id','identificacion','nombres','apellidos')

class DepartamentoAdmin(admin.ModelAdmin):
    list_display=('nomDepartamento','jefe')

class PersonalSoporteAdmin(admin.ModelAdmin):
    list_display=('id','identificacion','nombres','apellidos','email','direccion','telefonos')

class TicketAdmin(admin.ModelAdmin):
    list_display=('id','fechaReportado','fechaArreglado','cliente')
    
admin.site.register(Departamento, DepartamentoAdmin)

admin.site.register(Cliente,ClienteAdmin)

admin.site.register(PersonalSoporte, PersonalSoporteAdmin)

admin.site.register(Ticket, TicketAdmin)

admin.site.register(Parametro)

admin.site.register(ValorParametro)