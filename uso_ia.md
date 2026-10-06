# Uso de IA - Evaluación Sumativa 2

## Parte 1 - Registro de consultas

### Consulta 1 - Modelo
Se solicitó ayuda para transformar el catálogo de CrisSteel de una lista de productos escrita en la vista a un modelo Django llamado `Producto`, manteniendo los campos requeridos por la evaluación.

### Consulta 2 - Poblamiento
Se solicitó generar un poblamiento de 40 productos de ferretería en formato fixture JSON de Django, con `nombre`, `categoria`, `precio` y `stock`.

### Consulta 3 - Integración con la interfaz
Se solicitó adaptar las vistas para que el catálogo, el detalle y el punto de venta consultaran `Producto.objects` sin cambiar el diseño visual de CrisSteel.

### Ajustes realizados
Se mantuvieron las imágenes y plantillas de la ES1. Se agregó el modelo, la migración, el registro en Admin, la fixture `productos.json` y las consultas ORM. También se ajustó el stock que superaba el máximo solicitado por la pauta.

## Parte 2 - Explicación personal

**Esta sección debe ser escrita por el estudiante con sus propias palabras antes de entregar.**

Explica en 10 a 20 líneas qué le pediste a la IA, qué parte utilizaste, qué tuviste que corregir y qué aprendiste al pasar el catálogo desde datos estáticos a una base de datos.
