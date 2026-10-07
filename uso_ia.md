# Uso de IA - Evaluación Sumativa 2

## Parte 1 - Registro de consultas

### Consulta 1 - Modelo
Se solicitó ayuda para transformar el catálogo de CrisSteel de una lista de productos escrita en la vista a un modelo Django llamado `Producto`, manteniendo los campos requeridos por la evaluación.

### Consulta 2 - Poblamiento
**Prompt:** "Genera un poblamiento inicial de 40 productos de ferretería chilenos realistas para Django, con categorías, precios e inventario, listo para cargar mediante un comando ORM."

**Resumen de la respuesta:** se propuso un conjunto de datos distribuido entre categorías de ferretería y relacionado con precios, bodegas y movimientos de inventario.

**Uso y ajustes:** los datos se integraron en el comando idempotente `poblar_crisferreterias`, adaptándolos al esquema normalizado de MariaDB, donde el precio vigente y el stock se calculan desde entidades relacionadas.

### Consulta 3 - Integración con la interfaz
Se solicitó adaptar las vistas para que el catálogo, el detalle y el punto de venta consultaran `Producto.objects` sin cambiar el diseño visual de CrisSteel.

### Consulta 4 - Ruta principal y ejecución local
**Prompt:** "Haz que la página de la ferretería se abra en `http://127.0.0.1:8000/`, que ese enlace aparezca al ejecutar `python manage.py runserver` y que el proyecto cumpla lo solicitado en la pauta ES2."

**Resumen de la respuesta:** se revisaron la ruta raíz, el comando de desarrollo, los iniciadores y la documentación para dejar un único acceso local coherente.

**Uso y ajustes:** se confirmó que el catálogo se sirve desde `/`, se fijó el puerto predeterminado en 8000, se agregó un mensaje visible con la URL al iniciar Django y se actualizaron los archivos de ejecución y documentación.

### Ajustes realizados
Se mantuvieron las imágenes y plantillas de la ES1. Se agregó el modelo, la migración, el registro en Admin, la fixture `productos.json` y las consultas ORM. También se ajustó el stock que superaba el máximo solicitado por la pauta.

## Parte 2 - Explicación personal

**Esta sección debe ser escrita por el estudiante con sus propias palabras antes de entregar.**

Explica en 10 a 20 líneas qué le pediste a la IA, qué parte utilizaste, qué tuviste que corregir y qué aprendiste al pasar el catálogo desde datos estáticos a una base de datos.
