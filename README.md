# Inmobiliary Service

Este repositorio contiene el código fuente y los archivos necesarios para desplegar y ejecutar un servicio de gestión de inmobiliarias en un clúster de Kubernetes.

## Descripción

El servicio de inmobiliarias se dedica a la gestión de datos de inmobiliarias, permitiendo la creación, actualización, eliminación y consulta de inmobiliarias para facilitar su publicación y gestión en MercadoLibre.

## Índice

- [Proceso de Despliegue](#proceso-de-despliegue)
- [Uso del Servicio](#uso-del-servicio)
  - [Funcionalidades Principales](#funcionalidades-principales)
    - [Creación de Inmobiliaria](#creación-de-inmobiliaria)
    - [Actualización de Inmobiliaria](#actualización-de-inmobiliaria)
    - [Eliminación de Inmobiliaria](#eliminación-de-inmobiliaria)
    - [Obtener Inmobiliaria por ID](#obtener-inmobiliaria-por-id)
    - [Obtener Todas las Inmobiliarias](#obtener-todas-las-inmobiliarias)
- [Versiones Disponibles](#versiones-disponibles)
- [Contribución](#contribución)

## Proceso de Despliegue

Para desplegar el servicio de inmobiliarias en un clúster de Kubernetes, sigue los siguientes pasos:

1. **Configuración de Secrets para el servicio:** Crea un Secret en el clúster que contenga los siguientes datos:
   - `INMOBILIARY_COLLECTION`: Nombre para la colección de inmobiliarias dentro de la base de datos de MongoDB.
   - `DATABASE_NAME`: Nombre para la base de datos del proyecto.
   - `MONGO_URI`: URL del servidor de DB dentro del clúster.

2. **Configuración de Variables de Entorno:** Define las siguientes variables de entorno en tu flujo de trabajo de GitHub Actions o en tu entorno local:
   - `DOCKER_USERNAME`: Nombre de usuario de Docker Hub.
   - `DOCKER_PASSWORD`: Contraseña de Docker Hub.
   - `K8_NAMESPACE`: Nombre del namespace de Kubernetes donde se desplegará el servicio.
   - `K8_DEPLOYMENT`: Nombre del deployment de Kubernetes.
   - `K8_SECRET`: Nombre del secret donde se encuentran los datos del clúster.
   - `HPA_NAME`: Nombre del HPA (Horizontal Pod Autoscaler).
   - `SERVICE_NAME`: Nombre del servicio de Kubernetes.
   - `K8_APP`: Nombre de la aplicación.

3. **Ejecución del Flujo de Trabajo:** Ejecuta el flujo de trabajo de GitHub Actions `deploy.yml`. Este flujo de trabajo construirá la imagen del contenedor, la subirá a Docker Hub y luego aplicará los recursos de Kubernetes necesarios en el clúster.

4. **Verificación del Despliegue:** Una vez completado el flujo de trabajo, verifica que el servicio de inmobiliarias esté desplegado correctamente en tu clúster de Kubernetes.

## Uso del Servicio

El Servicio de Gestión de Inmobiliarias es una API RESTful diseñada para manejar la creación, actualización, eliminación y consulta de inmobiliarias. Este servicio está construido utilizando Flask y MongoDB para la persistencia de datos.

### Funcionalidades Principales:

#### Creación de Inmobiliaria
- **Ruta**: /create
- **Método**: POST
- **Descripción**: Crea una nueva inmobiliaria con los datos proporcionados.
- **Datos del Request**:
```json
{
  "nombre": "Inmobiliaria Ejemplo",
  "nombre_corporativo": "Inmobiliaria Ejemplo S.A.",
  "direccion": "Calle Falsa 123",
  "ciudad": "Ciudad Ejemplo",
  "estado": "Estado Ejemplo",
  "postal": "12345",
  "pais": "País Ejemplo",
  "telefono": "123456789",
  "email": "contacto@ejemplo.com",
  "web": "www.ejemplo.com",
  "logo": "link_logo",
  "fundacion": {"year": 2020, "month": 1, "day": 1},
  "propiedades": ["propiedad1", "propiedad2"]
}
```

#### Actualización de Inmobiliaria
- **Ruta**: /update/<inmobiliary_id>
- **Método**: PUT
- **Descripción**: Actualiza los datos de una inmobiliaria existente.
- **Datos del Request**:
```json
{
  "nombre": "Nuevo Nombre",
  "direccion": "Nueva Dirección",
  "ciudad": "Nueva Ciudad",
  "estado": "Nuevo Estado",
  "postal": "Nuevo Código Postal",
  "pais": "Nuevo País",
  "telefono": "Nuevo Teléfono",
  "email": "nuevoemail@ejemplo.com",
  "web": "www.nuevaweb.com",
  "logo": "link_nuevo_logo",
  "fundacion": {"year": 2021, "month": 2, "day": 2},
  "propiedades": ["nueva_propiedad1", "nueva_propiedad2"]
}
```

#### Eliminación de Inmobiliaria
- **Ruta**: /delete/<inmobiliary_id>
- **Método**: DELETE
- **Descripción**: Elimina una inmobiliaria por su ID.

#### Obtener Inmobiliaria por ID
- **Ruta**: /<inmobiliary_id>
- **Método**: GET
- **Descripción**: Obtiene los detalles de una inmobiliaria por su ID.

#### Obtener Todas las Inmobiliarias
- **Ruta**: /inmobiliarias
- **Método**: GET
- **Descripción**: Obtiene una lista de todas las inmobiliarias registradas.

## Versiones Disponibles

- **latest:** Última versión estable del servicio. Se recomienda su uso para entornos de producción.
- **v1.0:** Versión inicial del servicio.

Para cambiar la versión del servicio, modifica la etiqueta de imagen del contenedor en el archivo `deploy.yml` antes de ejecutar el flujo de trabajo.

## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama para tu contribución (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commits (`git commit -am 'Agrega nueva funcionalidad'`).
4. Sube tus cambios a tu repositorio remoto (`git push origin feature/nueva-funcionalidad`).
5. Crea un nuevo pull request en GitHub.

Esperamos tus contribuciones!
