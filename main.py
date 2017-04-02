import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import app_identity
from google.appengine.api import images
from google.appengine.ext import blobstore
import cloudstorage
import mimetypes
import json
import os
import jinja2
from google.appengine.api import mail, taskqueue

from models import Empresa, Servicio, Introduccion
from models import Team, Acerca, Caracteristica, Ubicacion

jinja_env = jinja2.Environment(
 loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class DemoClass(object):
 pass

def MyClass(obj):
 return obj.__dict__


class GetTeamHandler(webapp2.RequestHandler):

    def get(self):
     self.response.headers.add_header('Access-Control-Allow-Origin', '*')
     self.response.headers['Content-Type'] = 'application/json'

     id_empresa = self.request.get('empresa')
     objemp = Empresa.query(Empresa.codigo_empresa == id_empresa).get()
     strKey = objemp.key.urlsafe() 
     myEmpKey = ndb.Key(urlsafe=strKey) 
     myTeam = Team.query(Team.empresa_key == myEmpKey)

     myList = []
     for i in myTeam:
      myObj = DemoClass()
      myObj.entityKey = i.entityKey
      myObj.nombre = i.nombre
      myObj.puesto = i.puesto
      myObj.urlImage = i.urlImage
      myList.append(myObj)
       
     json_string = json.dumps(myList, default=MyClass)
     self.response.write(json_string)

class GetServicioHandler(webapp2.RequestHandler):

    def get(self):
     self.response.headers.add_header('Access-Control-Allow-Origin', '*')
     self.response.headers['Content-Type'] = 'application/json'

     id_empresa = self.request.get('empresa')
     objemp = Empresa.query(Empresa.codigo_empresa == id_empresa).get()
     strKey = objemp.key.urlsafe() 
     myEmpKey = ndb.Key(urlsafe=strKey) 
     myServicio = Servicio.query(Servicio.empresa_key == myEmpKey)

     myList = []
     for i in myServicio:
      myObj = DemoClass()
      myObj.entityKey = i.entityKey
      myObj.nombre = i.nombre
      myObj.descripcion = i.descripcion
      myObj.urlImage = i.urlImage
      myList.append(myObj)
       
     json_string = json.dumps(myList, default=MyClass)
     self.response.write(json_string)


class GetIntroduccionHandler(webapp2.RequestHandler):

    def get(self):
     self.response.headers.add_header('Access-Control-Allow-Origin', '*')
     self.response.headers['Content-Type'] = 'application/json'

     id_empresa = self.request.get('empresa')
     objemp = Empresa.query(Empresa.codigo_empresa == id_empresa).get()
     strKey = objemp.key.urlsafe() 
     myEmpKey = ndb.Key(urlsafe=strKey) 
     myIntroduccion = Introduccion.query(Introduccion.empresa_key == myEmpKey)

     myList = []
     for i in myIntroduccion:
      myObj = DemoClass()
      myObj.entityKey = i.entityKey
      myObj.nombre = i.nombre
      myObj.descripcion = i.descripcion
      myObj.urlImage = i.urlImage
      myList.append(myObj)
       
     json_string = json.dumps(myList, default=MyClass)
     self.response.write(json_string)

class GetAcercaHandler(webapp2.RequestHandler):

    def get(self):
     self.response.headers.add_header('Access-Control-Allow-Origin', '*')
     self.response.headers['Content-Type'] = 'application/json'

     id_empresa = self.request.get('empresa')
     objemp = Empresa.query(Empresa.codigo_empresa == id_empresa).get()
     strKey = objemp.key.urlsafe() 
     myEmpKey = ndb.Key(urlsafe=strKey) 
     myAcerca = Acerca.query(Acerca.empresa_key == myEmpKey)

     myList = []
     for i in myAcerca:
      myObj = DemoClass()
      myObj.entityKey = i.entityKey
      myObj.nombre = i.nombre
      myObj.descripcion = i.descripcion
      myObj.urlImage = i.urlImage
      myList.append(myObj)
       
     json_string = json.dumps(myList, default=MyClass)
     self.response.write(json_string)

class GetCaracteristicaHandler(webapp2.RequestHandler):

    def get(self):
     self.response.headers.add_header('Access-Control-Allow-Origin', '*')
     self.response.headers['Content-Type'] = 'application/json'

     id_empresa = self.request.get('empresa')
     objemp = Empresa.query(Empresa.codigo_empresa == id_empresa).get()
     strKey = objemp.key.urlsafe() 
     myEmpKey = ndb.Key(urlsafe=strKey) 
     myCaracteristica = Caracteristica.query(Caracteristica.empresa_key == myEmpKey)

     myList = []
     for i in myCaracteristica:
      myObj = DemoClass()
      myObj.entityKey = i.entityKey
      myObj.nombre = i.nombre
      myObj.descripcion = i.descripcion
      myObj.urlImage = i.urlImage
      myList.append(myObj)
       
     json_string = json.dumps(myList, default=MyClass)
     self.response.write(json_string)
class GetUbicacionHandler(webapp2.RequestHandler):

    def get(self):
     self.response.headers.add_header('Access-Control-Allow-Origin', '*')
     self.response.headers['Content-Type'] = 'application/json'

     id_empresa = self.request.get('empresa')
     objemp = Empresa.query(Empresa.codigo_empresa == id_empresa).get()
     strKey = objemp.key.urlsafe() 
     myEmpKey = ndb.Key(urlsafe=strKey) 
     myUbicacion = Ubicacion.query(Ubicacion.empresa_key == myEmpKey)

     myList = []
     for i in myUbicacion:
      myObj = DemoClass()
      myObj.entityKey = i.entityKey
      myObj.latitud = i.latitud
      myObj.longitud = i.longitud
      myList.append(myObj)
       
     json_string = json.dumps(myList, default=MyClass)
     self.response.write(json_string)
###########################################################################     


class UpHandler(webapp2.RequestHandler):
    def _get_urls_for(self, file_name):
        
     bucket_name = app_identity.get_default_gcs_bucket_name()
     path = os.path.join('/', bucket_name, file_name)
     real_path = '/gs' + path
     key = blobstore.create_gs_key(real_path)
     try:
      url = images.get_serving_url(key, size=0)
     except images.TransformationError, images.NotImageError:
      url = "http://storage.googleapis.com{}".format(path)

     return url


    def post(self):
     self.response.headers.add_header('Access-Control-Allow-Origin', '*')
     self.response.headers['Content-Type'] = 'application/json'

     bucket_name = app_identity.get_default_gcs_bucket_name()
     uploaded_file = self.request.POST.get('uploaded_file')
     file_name = getattr(uploaded_file, 'filename', None)
     file_content = getattr(uploaded_file, 'file', None)
     real_path = ''

     if file_name and file_content:
      content_t = mimetypes.guess_type(file_name)[0]
      real_path = os.path.join('/', bucket_name, file_name)

      with cloudstorage.open(real_path, 'w', content_type=content_t,
       options={'x-goog-acl': 'public-read'}) as f:
       f.write(file_content.read())

      key = self._get_urls_for(file_name)
      self.response.write(key)


class LoginHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('login.html', template_context))

   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)


class MenuHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('menu.html', template_context))

   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)

class EditaServicioHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('editaservicio.html', template_context))

   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)
    
class AdminHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('admin.html', template_context))

   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)
class MapaHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('mapa.html', template_context))

   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)

class AdminServicioHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('servicio.html', template_context))

   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)

class ActualizaServicioHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('actualizaservicio.html', template_context))

   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)

class AdminIntroduccionHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('introduccion.html', template_context))

   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)

class AdminAcercaHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('acerca.html', template_context))

   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)

class AdminCaracteristicaHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('caracteristica.html', template_context))

   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)

class MainHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('index.html', template_context))


   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)

class AdminMapaHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('adminmapa.html', template_context))


   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)

class ListaTeamHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('listateam.html', template_context))


   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)

class ListaIntroduccionHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('listaintroduccion.html', template_context))


   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)

class ListaAcercaHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('listaacerca.html', template_context))


   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)

class ListaCaracteristicaHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('listacaracteristica.html', template_context))


   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)

class ListaUbicacionHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('listaubicacion.html', template_context))


   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)

class EditaTeamHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('editateam.html', template_context))


   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)

class EditaIntroduccionHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('editaintroduccion.html', template_context))


   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)
class EditaAcercaHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('editaacerca.html', template_context))


   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)

class EditaCaracteristicaHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('editacaracteristica.html', template_context))


   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)

class EditaUbicacionHandler(webapp2.RequestHandler):

   def get(self):

    template_context = {}
    self.response.out.write(
      self._render_template('editaubicacion.html', template_context))


   def _render_template(self, template_name, context=None):
    if context is None:
     context = {}

    template = jinja_env.get_template(template_name)
    return template.render(context)


class SendTaskMail(webapp2.RequestHandler):
    def post(self):
        name = self.request.get('name')
        email = self.request.get('email')
        content = self.request.get('content')
        sender =self.request.get('sender_address')
        send_approved_mail(sender, name, email, content)

class SendMessageHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers.add_header('Access-Control-Allow-Origin', '*')
        self.response.headers['Content-Type'] = 'application/json'

        name = self.request.get('name')
        email = self.request.get('email')
        content = self.request.get('message')
        sender = "admin@segundoparcial-7.appspotmail.com".format(app_identity.get_application_id())
        taskqueue.add(url='/sendtask',
                     params={'sender_address': sender, 'name': name, 'email': email, 'content': content})
        json_string = json.dumps("true", default=MyClass)
        self.response.write(json_string)

def send_approved_mail(sender_address, name, email, content):
    # [START send_message]
    message = mail.EmailMessage(
        sender=sender_address,
        subject="Message by " + name + " from " + email)

    message.to = "Heloel Hernandez <heloelhdez@gmail.com>"
    message.body = content
    message.send()
    # [END send_message]

class CronJob(webapp2.RequestHandler):

    def get(self):

        
        empresas = Empresa.query().fetch()

        myList = []
        for i in empresas:
            empObj = DemoClass()
            empObj.nombre = i.nombre_empresa
            empObj.codigo = i.codigo_empresa
            empObj.id_empresa = i.entityKey
        
            myList.append(empObj.nombre)

            emp_key = ndb.Key(urlsafe=empObj.id_empresa)
            objemp = emp_key.get()
            strKey = objemp.key.urlsafe() 
            myEmpKey = ndb.Key(urlsafe=strKey) 
            myservicio = Servicio.query(Servicio.empresa_key == myEmpKey)

            for i in myservicio:
                artObj = DemoClass()
                artObj.nombre = i.nombre
                artObj.descripcion = i.descripcion
                myList.append(artObj.nombre)
                myList.append("\n")




        serviciosText =  "\n".join(str(x) for x in myList)

        fileName = "/servicios.txt"

        try:
            with cloudstorage.open(fileName, "r") as gcsFile:
                tempStorage = gcsFile.read()
                tempStorage += "\n"
        except:
            tempStorage = ""

        with cloudstorage.open(fileName, "w") as gcsFile:
            gcsFile.write(str(serviciosText))
            # gcsFile.write(tempStorage + str(serviciosText))

        with cloudstorage.open(fileName, "r") as gcsFile:
            output=  gcsFile.read()  
        self.response.out.write(output)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login', LoginHandler),
    ('/menu', MenuHandler),
    ('/admin', AdminHandler),
    ('/up', UpHandler),
    ('/getteam', GetTeamHandler),
    ('/menu', MenuHandler),
    ('/getservicio', GetServicioHandler),
    ('/adminservicio', AdminServicioHandler),
    ('/editaservicio', EditaServicioHandler),
    ('/actualizaservicio', ActualizaServicioHandler),
    ('/getintroduccion', GetIntroduccionHandler),
    ('/adminintroduccion', AdminIntroduccionHandler),
    ('/getacerca', GetAcercaHandler),
    ('/adminacerca', AdminAcercaHandler),
    ('/getcaracteristica', GetCaracteristicaHandler),
    ('/admincaracteristica', AdminCaracteristicaHandler),
    ('/mapa', MapaHandler),
    ('/adminmapa', AdminMapaHandler),
    ('/getubicacion',GetUbicacionHandler),
    ('/listateam',ListaTeamHandler),
    ('/editateam',EditaTeamHandler),
    ('/listaintroduccion',ListaIntroduccionHandler),
    ('/listaacerca',ListaAcercaHandler),
    ('/listaubicacion',ListaUbicacionHandler),
    ('/editaintroduccion',EditaIntroduccionHandler),
    ('/editaacerca',EditaAcercaHandler),
    ('/editacaracteristica',EditaCaracteristicaHandler),
    ('/editaubicacion',EditaUbicacionHandler),
    ('/listacaracteristica',ListaCaracteristicaHandler),
    ('/sendmail', SendMessageHandler),
    ('/sendtask', SendTaskMail),
    ('/cronjob', CronJob),
    
 
], debug = True)
