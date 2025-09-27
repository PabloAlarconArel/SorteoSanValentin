# SorteoSanValentin
### Descripción
Este proyecto consiste en la realización de una aplicación Full Stack para gestionar un sorteo de san Valentín.
Desarrollado con las herramientas de **Django** y **Vue.js** comunicándose por medio de API REST.

## Instalación y ejecución

### Backend (Django)

1. Clonar Repositorio
   ```bash
   git clone <URLdelRepositorio>
   cd Backend
   ```
2.Crear un entorno virtual
```bash
python -m venv venv
venv\scripts\activate
# O tambien con Conda
conda create -n <nombreDetEntorno> python = <versión estimada> -y
conda activate  <nombreDetuVEntorno>
```
3.Instalar dependencias
```bash
pip install -r requirements.txt
```
4.Configurar variables de entorno
```bash
SECRET_KEY=<tu_secret_key>
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```
5.Migrar la base de datos
```bash
python manage.py makemigrations
python manage.py migrate
```
6.Ejecutar el serviodor
```bash
python manage.py runserver
```
El server esta diponible en http://localhost:8000/

### Fronted (vue.js)
1.Crear directorio fronted
```bash
mkdir fronted
cd fronted
```
2.Instalar Vue CLI
```bash
npm install -g @vue/cli
```
3.Crear un nuevo proyecto
```bash
vue create nombre-del-proyecto
```
Te preguntará:
Presets predeterminados (Default: Babel + ESLint)
Configuración manual (para elegir Router, Vuex, TypeScript, etc.)

4. Ejecutar el poryecto en modo desarrollo
```bash
cd nombre-del-proyecto
npm run serve
```
Por defecto, estará disponible en http://localhost:8080/
Cada cambio que hagas se reflejará automáticamente en el navegador (hot reload).


## Decisiones técnicas

- ***Vue.js 3 + Composition API***: para trabajar con las últimas tendencias del fronted
- ***Axios***: Para manejar las llamadas HTTP entre frontend y backend.
- ***Serializers***: se utlizó para validaciones de los datos enviados.Ademas de evitar demasiados condicionales para verificar.
- ***Form***: Opción escogida para manejar formularios y evitar ciertas validaciones manuales y más específicas como clean_field
- ***Componentes reutilizables***: Como tablas y sidebar para su reutilización en otros vistas.
- *** tablas ***: uso de la librería vue-good-table para mostrar de forma ordenada los participantes.

## Endpoint Principales

1. Registro de usuario
Post api/register/

Request:
```bash
{
  "Full_name": "Pablo Javier Peña",
  "email": "usuario1@mail.com",
  "password": "codssdsdt123"
}
```
Response:
```bash
{"message":"¡Gracias por registrarte! Revisa tu correo para verificar tu cuenta."}
```

2.Login
Post api/login
Request
```bash
{
  "email": "usuario1@mail.com",
  "password": "codssdsdt123"
}
```
Response:
```bash
  {
  "message":"login exitoso",
  "refresh":str(refresh),
  "access":str(refresh.access_token)           
  }
```
3.Seleccionar ganador 
  Get api/select-winner/
```bash
  {
    "message":"Ganador seleccionado",
    "winner": {
        "full_name": winner.full_name,
        "email": winner.email,
    }
}
```
4.verificar correo
  Post api/verify/
  
  Request
```bash
  {
  "password": "MiPasswordSegura123",
  "password_confirm": "MiPasswordSegura123"
}
```
Response
```bash
  {
  "mensaje": "Tu cuenta ha sido activada. Ya estás participando en el sorteo."
}
```
## ScreenShoots




<img width="1546" height="777" alt="cts inicio" src="https://github.com/user-attachments/assets/087c52cb-3fdb-43c7-a8e8-e6b123b624bb" />






