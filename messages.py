from protorpc import messages
from protorpc import message_types

class MessageNone(messages.Message):
    inti = messages.StringField(1)
# Input messages
#Recibe el token para validar
class Token(messages.Message):
    tokenint = messages.StringField(1, required=True)
    #entityKey = messages.StringField(2, required=False)
    #fromurl = messages.StringField(3)

#Recibe el token y un entityKey de cualquier base de datos para validar
class TokenKey(messages.Message):
    tokenint = messages.StringField(1, required=True)
    entityKey = messages.StringField(2, required=True)
    #fromurl = messages.StringField(3)


#Recibe el email y contrasena para la creacion de token
class EmailPasswordMessage(messages.Message):
    email = messages.StringField(1, required=True)
    password = messages.StringField(2, required=True)


#USERS
class UserInput(messages.Message):
    token = messages.StringField(1) 
    empresa_key = messages.StringField(2)
    email = messages.StringField(3)
    password = messages.StringField(4)



class UserUpdate(messages.Message):
    token = messages.StringField(1)
    email = messages.StringField(2)
    password = messages.StringField(3)
    entityKey = messages.StringField(4, required=True)

class UserList(messages.Message):
    code = messages.IntegerField(1)
    data = messages.MessageField(UserUpdate, 2, repeated=True)


######Empresa########

#Mensaje de Entrada y Salida para la base de datos Empresa
class EmpresaInput(messages.Message):
    token = messages.StringField(1, required=True) 
    codigo_empresa = messages.StringField(2)
    nombre_empresa = messages.StringField(3)


class EmpresaUpdate(messages.Message):
    token = messages.StringField(1, required=True)
    entityKey = messages.StringField(2, required=True)
    codigo_empresa = messages.StringField(3)
    nombre_empresa = messages.StringField(4)



#regresa una lista para la base de datos Empresa
class EmpresaList(messages.Message):
    code = messages.IntegerField(1)
#regresa mensaje de lo ocurrido
#mensaje de tipo MENSAJEFIELD que regresa una lista de tipo EmpresaUpdate
#es necesario el repeated para que sea lista
    data = messages.MessageField(EmpresaUpdate, 2, repeated=True)

######Team########

#Mensaje de Entrada y Salida para la base de datos Team
class TeamInput(messages.Message):
    token = messages.StringField(1, required=True) 
    nombre = messages.StringField(2)
    puesto = messages.StringField(3)
    urlImage = messages.StringField(5)

    
class TeamUpdate(messages.Message):
    token = messages.StringField(1, required=True)
    #empresa_key = messages.StringField(2, required=True)
    entityKey = messages.StringField(2, required=True)
    nombre = messages.StringField(3)
    puesto = messages.StringField(4)
    urlImage = messages.StringField(5)

#regresa una lista para la base de datos Empresa
class TeamList(messages.Message):
    code = messages.IntegerField(1)
#regresa mensaje de lo ocurrido
#mensaje de tipo MENSAJEFIED que regresa una lista de tipo TeamUpdate
#es necesario el repeated para que sea lista
    data = messages.MessageField(TeamUpdate, 2, repeated=True)

######Servicio########

#Mensaje de Entrada y Salida para la base de datos Team
class ServicioInput(messages.Message):
    token = messages.StringField(1, required=True) 
    nombre = messages.StringField(2)
    descripcion = messages.StringField(3)
    urlImage = messages.StringField(5)

    
class ServicioUpdate(messages.Message):
    token = messages.StringField(1, required=True)
    #empresa_key = messages.StringField(2, required=True)
    entityKey = messages.StringField(2, required=True)
    nombre = messages.StringField(3)
    descripcion = messages.StringField(4)
    urlImage = messages.StringField(5)

#regresa una lista para la base de datos Empresa
class ServicioList(messages.Message):
    code = messages.IntegerField(1)
#regresa mensaje de lo ocurrido
#mensaje de tipo MENSAJEFIED que regresa una lista de tipo TeamUpdate
#es necesario el repeated para que sea lista
    data = messages.MessageField(ServicioUpdate, 2, repeated=True)

######Introduccion########

#Mensaje de Entrada y Salida para la base de datos Team
class IntroduccionInput(messages.Message):
    token = messages.StringField(1, required=True) 
    nombre = messages.StringField(2)
    descripcion = messages.StringField(3)
    urlImage = messages.StringField(5)

    
class IntroduccionUpdate(messages.Message):
    token = messages.StringField(1, required=True)
    #empresa_key = messages.StringField(2, required=True)
    entityKey = messages.StringField(2, required=True)
    nombre = messages.StringField(3)
    descripcion = messages.StringField(4)
    urlImage = messages.StringField(5)

#regresa una lista para la base de datos Empresa
class IntroduccionList(messages.Message):
    code = messages.IntegerField(1)
#regresa mensaje de lo ocurrido
#mensaje de tipo MENSAJEFIED que regresa una lista de tipo TeamUpdate
#es necesario el repeated para que sea lista
    data = messages.MessageField(IntroduccionUpdate, 2, repeated=True)

######Acerca########

#Mensaje de Entrada y Salida para la base de datos Team
class AcercaInput(messages.Message):
    token = messages.StringField(1, required=True) 
    nombre = messages.StringField(2)
    descripcion = messages.StringField(3)
    urlImage = messages.StringField(5)

    
class AcercaUpdate(messages.Message):
    token = messages.StringField(1, required=True)
    #empresa_key = messages.StringField(2, required=True)
    entityKey = messages.StringField(2, required=True)
    nombre = messages.StringField(3)
    descripcion = messages.StringField(4)
    urlImage = messages.StringField(5)

#regresa una lista para la base de datos Empresa
class AcercaList(messages.Message):
    code = messages.IntegerField(1)
#regresa mensaje de lo ocurrido
#mensaje de tipo MENSAJEFIED que regresa una lista de tipo TeamUpdate
#es necesario el repeated para que sea lista
    data = messages.MessageField(AcercaUpdate, 2, repeated=True)

######Caracteristica########

#Mensaje de Entrada y Salida para la base de datos Team
class CaracteristicaInput(messages.Message):
    token = messages.StringField(1, required=True) 
    nombre = messages.StringField(2)
    descripcion = messages.StringField(3)
    urlImage = messages.StringField(5)

    
class CaracteristicaUpdate(messages.Message):
    token = messages.StringField(1, required=True)
    #empresa_key = messages.StringField(2, required=True)
    entityKey = messages.StringField(2, required=True)
    nombre = messages.StringField(3)
    descripcion = messages.StringField(4)
    urlImage = messages.StringField(5)

#regresa una lista para la base de datos Empresa
class CaracteristicaList(messages.Message):
    code = messages.IntegerField(1)
#regresa mensaje de lo ocurrido
#mensaje de tipo MENSAJEFIED que regresa una lista de tipo TeamUpdate
#es necesario el repeated para que sea lista
    data = messages.MessageField(CaracteristicaUpdate, 2, repeated=True)

######Ubicacion########

#Mensaje de Entrada y Salida para la base de datos Team
class UbicacionInput(messages.Message):
    token = messages.StringField(1, required=True) 
    latitud = messages.StringField(2)
    longitud = messages.StringField(3)
    

    
class UbicacionUpdate(messages.Message):
    token = messages.StringField(1, required=True)
    #empresa_key = messages.StringField(2, required=True)
    entityKey = messages.StringField(2, required=True)
    latitud = messages.StringField(3)
    longitud = messages.StringField(4)
    

#regresa una lista para la base de datos Empresa
class UbicacionList(messages.Message):
    code = messages.IntegerField(1)
#regresa mensaje de lo ocurrido
#mensaje de tipo MENSAJEFIED que regresa una lista de tipo TeamUpdate
#es necesario el repeated para que sea lista
    data = messages.MessageField(UbicacionUpdate, 2, repeated=True)



# Output messages
#regresa un token
class TokenMessage(messages.Message):
    code = messages.IntegerField(1)
    message = messages.StringField(2)
    token = messages.StringField(3)

#regresa mensajes de lo ocurrido
class CodeMessage(messages.Message):
    code = messages.IntegerField(1)
    message = messages.StringField(2)




