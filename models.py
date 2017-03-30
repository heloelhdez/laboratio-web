import base64
import Crypto
from Crypto.Hash import SHA256
from google.appengine.ext import ndb
from google.appengine.ext import blobstore
from protorpc import remote
from endpoints_proto_datastore.ndb import EndpointsModel
import endpoints
from google.appengine.api import mail
from google.appengine.ext.webapp import blobstore_handlers

class CustomBaseModel(EndpointsModel):
    def populate(self, data):
        super(self.__class__, self).__init__()
        for attr in self._message_fields_schema:
            if hasattr(data, attr):
                setattr(self, attr, getattr(data, attr))

## empresa
class Empresa(CustomBaseModel):
    _message_fields_schema = ('entityKey', 'codigo_empresa', 'nombre_empresa')
    codigo_empresa = ndb.StringProperty()
    nombre_empresa = ndb.StringProperty()
    
       ###Empresa####
    def empresa_m(self, data):
        empresa = Empresa()#Crea una variable de tipo Base de datos
        empresa.populate(data)#Llena la variables con los datos dados por el request en main.py
        #empresa.empresa_key=empresakey #inserta el entityKey de la empresa que es un parametro que se manda en main.py
        empresa.put()#inserta o hace un update depende del main.py
        return 0



#####USUARIOS#########

class Usuarios(CustomBaseModel):
    _message_fields_schema = ('entityKey', 'email', 'password', 'salt')

    empresa_key = ndb.KeyProperty(kind=Empresa)
    email = ndb.StringProperty()
    password = ndb.StringProperty()
    salt = ndb.StringProperty(indexed=False)
   
 
    def hash_password(self):
        """ Create a cryptographyc random secure salt and hash the password
            using the salt created and store both in the database, the password
            and the salt """
        # Note: It is needed to encode in base64 the salt, otherwise it will
        # cause an exception trying to store non utf-8 characteres
        self.salt = base64.urlsafe_b64encode(
            Crypto.Random.get_random_bytes(16))
        hash_helper = SHA256.new()
        hash_helper.update(self.password + self.salt)
        self.password = hash_helper.hexdigest()

    def verify_password(self, password):
        """ Verify if the password is correct """
        hash_helper = SHA256.new()
        hash_helper.update(password + self.salt)
        return hash_helper.hexdigest() == self.password

       ###Usuarios####
    def usuario_m(self, data, empresakey):
        user = Usuarios()#Crea una variable de tipo Base de datos
        user.populate(data)#Llena la variables con los datos dados por el request en main.py
        user.empresa_key=empresakey
        user.status=1
        user.hash_password()#encripta la contrasena
        user.put()#inserta o hace un update depende del main.py
        return 0




def validarEmail(email):
	emailv = Usuarios.query(Usuarios.email == email)
	if not emailv.get():
		return False
	else:
		return True

if validarEmail("root@kubeet.com") == False:
    empresaAdmin = Empresa(
      codigo_empresa = 'kubeet',
      nombre_empresa="kubeet sa de cv",
 	 
    )
    empresaAdmin.put()
    keyadmincol = ndb.Key(urlsafe=empresaAdmin.entityKey)
    admin = Usuarios(
          empresa_key = keyadmincol,
	      email="root@kubeet.com",
          password="docker",
       
    )
    admin.hash_password()
    admin.put()

######### Team #########

class Team(CustomBaseModel):
    _message_fields_schema = ('entityKey', 'nombre', 'puesto', 'urlImage')
    empresa_key = ndb.KeyProperty(kind=Empresa)
    nombre = ndb.StringProperty()
    puesto = ndb.StringProperty()
    urlImage = ndb.StringProperty()
 
    ### Team ####
    def team_m(self, data, empresakey):
        team  = Team()#Crea una variable de tipo Base de datos
        team.populate(data)#Llena la variables con los datos dados por el request en main.py
        team.empresa_key=empresakey#inserta el entityKey de la empresa que es un parametro que se manda en main.py
        team.put()#inserta o hace un update depende del main.py
        return 0

######### Servicio #########

class Servicio(CustomBaseModel):
    _message_fields_schema = ('entityKey', 'nombre', 'descripcion', 'urlImage')
    empresa_key = ndb.KeyProperty(kind=Empresa)
    nombre = ndb.StringProperty()
    descripcion = ndb.StringProperty()
    urlImage = ndb.StringProperty()
 
    ### Servicio ####
    def servicio_m(self, data, empresa_key):
        servicio  = Servicio()#Crea una variable de tipo Base de datos
        servicio.populate(data)#Llena la variables con los datos dados por el request en main.py
        servicio.empresa_key=empresa_key#inserta el entityKey de la empresa que es un parametro que se manda en main.py
        servicio.put()#inserta o hace un update depende del main.py
        return 0


####### Introduccion #########

class Introduccion(CustomBaseModel):
    _message_fields_schema = ('entityKey', 'nombre', 'descripcion', 'urlImage')
    empresa_key = ndb.KeyProperty(kind=Empresa)
    nombre = ndb.StringProperty()
    descripcion = ndb.StringProperty()
    urlImage = ndb.StringProperty()
 
    ### Intro ####
    def introduccion_m(self, data, empresa_key):
        introduccion  = Introduccion()#Crea una variable de tipo Base de datos
        introduccion.populate(data)#Llena la variables con los datos dados por el request en main.py
        introduccion.empresa_key=empresa_key#inserta el entityKey de la empresa que es un parametro que se manda en main.py
        introduccion.put()#inserta o hace un update depende del main.py
        return 0


####### Acerca #########

class Acerca(CustomBaseModel):
    _message_fields_schema = ('entityKey', 'nombre', 'descripcion', 'urlImage')
    empresa_key = ndb.KeyProperty(kind=Empresa)
    nombre = ndb.StringProperty()
    descripcion = ndb.StringProperty()
    urlImage = ndb.StringProperty()
 
    ### Acerca ####
    def acerca_m(self, data, empresa_key):
        acerca  = Acerca()#Crea una variable de tipo Base de datos
        acerca.populate(data)#Llena la variables con los datos dados por el request en main.py
        acerca.empresa_key=empresa_key#inserta el entityKey de la empresa que es un parametro que se manda en main.py
        acerca.put()#inserta o hace un update depende del main.py
        return 0

####### Caracteristica #########

class Caracteristica(CustomBaseModel):
    _message_fields_schema = ('entityKey', 'nombre', 'descripcion', 'urlImage')
    empresa_key = ndb.KeyProperty(kind=Empresa)
    nombre = ndb.StringProperty()
    descripcion = ndb.StringProperty()
    urlImage = ndb.StringProperty()
 
    ### Acerca ####
    def caracteristica_m(self, data, empresa_key):
        caracteristica  = Caracteristica()#Crea una variable de tipo Base de datos
        caracteristica.populate(data)#Llena la variables con los datos dados por el request en main.py
        caracteristica.empresa_key=empresa_key#inserta el entityKey de la empresa que es un parametro que se manda en main.py
        caracteristica.put()#inserta o hace un update depende del main.py
        return 0