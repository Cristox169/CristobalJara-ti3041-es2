# CrisSteel · CrisFerreterias

Sistema Django integral para una ferretería, construido sobre el proyecto ES2 original y conectado exclusivamente a MariaDB. Cubre catálogo, punto de venta persistente, compras, inventario, logística, recursos humanos, nómina, producción y análisis financiero.

## Base de datos

- Motor: MariaDB 11.4.3.
- Base: `CrisFerreterias`.
- Puerto local: `3307`, separado del MariaDB incluido en XAMPP.
- Juego de caracteres: `utf8mb4`.
- Configuración privada: `.env` (ignorada por Git).
- Esquema normalizado: [`docs/normalizacion_5fn.md`](docs/normalizacion_5fn.md).
- Consultas analíticas: [`connectBD/consultas.sql`](connectBD/consultas.sql).

`Producto` no almacena precio ni stock. El precio vigente se obtiene desde `PrecioProducto` y el inventario se deriva de `MovimientoInventario`. Las relaciones multivaluadas están descompuestas mediante tablas puente y los documentos usan cabecera/detalle.

## Inicio rápido

Desde la carpeta del proyecto:

```powershell
.\scripts\iniciar_mariadb.ps1
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py poblar_crisferreterias
.\.venv\Scripts\python.exe manage.py runserver
```

O ejecutar `iniciar_crissteel.bat`, que verifica dependencias, inicia MariaDB, aplica migraciones y carga los datos sin duplicarlos.

Sitio: <http://127.0.0.1:8000/>

Administración: <http://127.0.0.1:8000/admin/>

## Módulos

- `/` — catálogo de 40 productos obtenidos desde MariaDB.
- `/panel/` — indicadores generales.
- `/punto-de-venta/` — venta real en base de datos y descuento transaccional de stock.
- `/ventas/` — ingresos, costos y margen.
- `/logistica/` — bodegas, compras, movimientos y alertas.
- `/personas/` — empleados, cargos, contratos y nómina.
- `/produccion/` — recetas, órdenes y consumos.
- `/finanzas/` — ingresos, costos, gastos y resultado.
- `/api/productos/` — API JSON derivada del esquema normalizado.
- `/configuracion/` — motor, versión, base activa y accesos.
- `/admin/` — CRUD completo de todas las entidades.

## Verificación

```powershell
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py makemigrations --check --dry-run
.\.venv\Scripts\python.exe manage.py test catalogo
```

El comando `poblar_crisferreterias` es idempotente. Carga 40 productos, precios, inventario por bodega, proveedores, compras, ventas, clientes, personal, nómina, producción, despachos y transacciones financieras.

El archivo `uso_ia.md` registra las consultas y ajustes realizados con IA. La Parte 2 debe completarla personalmente el estudiante, tal como exige la pauta.
