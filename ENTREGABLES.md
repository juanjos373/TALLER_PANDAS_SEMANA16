# Entregables — Taller práctico de Pandas

**Estudiante:** Juan Joé Sáenz

## Entregable 0: ambiente virtual

El ambiente `venv` se creó y se instalaron las dependencias declaradas en `requirements.txt`:

- pandas 3.0.2
- matplotlib 3.10.8
- seaborn 0.13.2

La captura de terminal debe mostrar el ambiente activo (`(venv)`) y el final de la instalación.

## Entregable 1: exploración

La ejecución de `python exploracion.py` reporta:

- Clientes: forma `(60, 5)`. Las cinco columnas tienen 60 valores no nulos; `id_cliente` es entero y las demás columnas son texto. Para `id_cliente`: media 30.5, mínimo 1 y máximo 60.
- Ventas: forma `(68, 10)`. `producto` tiene 67 valores no nulos; las demás columnas tienen 68. Las columnas numéricas son `id_cliente`, `cantidad`, `precio_unitario` y `total`.
- En ventas, `cantidad` tiene media 1.3088 y rango de 1 a 4; `total` tiene media de 282,000, mínimo de 18,000 y máximo de 2,450,000.
- La salida completa de `.info()`, `.describe()` y de los ejemplos de indexación está disponible al ejecutar el script.

**¿Por qué `.iloc[2, 6]` devuelve el total de V003?** Después de usar `id_venta` como índice, ya no se cuenta como columna. La fila 2 es V003 y la columna en posición 6, contando desde cero, es `total`; por eso devuelve `520000`.

Los rangos también demuestran que `.loc['V001':'V006']` incluye ambos extremos, mientras que `.iloc[0:5]` incluye las posiciones 0 a 4. La separación por mes produjo 60 ventas de abril y 8 de mayo; `concat()` volvió a reunir las 68.

## Entregable 2: limpieza

Antes de limpiar había 60 clientes y 68 ventas. No se encontraron filas duplicadas en ninguno de los archivos. En ventas se encontró un producto vacío; se reemplazó por `Sin especificar` para conservar la venta y su valor. Las fechas se convirtieron al tipo fecha y se reiniciaron los índices después de eliminar posibles duplicados. No se eliminaron filas: quedaron 60 clientes y 68 ventas. La columna `fecha_venta` se verifica como `datetime64[us]` después de la limpieza.

## Entregable 3, parte 1: validación y merge

Las validaciones confirmaron que `id_cliente` existe en las dos tablas, no está duplicado en clientes y tiene tipo `int64` en ambas. No hubo ventas sin cliente asociado. El merge produjo **68 filas y 14 columnas**.

La tabla unida tiene 14 columnas porque clientes aporta 5, ventas aporta 10 y `id_cliente` es la columna común: `5 + 10 - 1 = 14`. Se conserva el número de ventas porque se utiliza una unión `left`, con ventas como tabla de la izquierda.

El resultado se guarda en `Data/processed/merge.csv`.

## Entregable 3, parte 2: análisis y desafío final

Los resultados se calcularon sobre las 68 ventas ya limpias y unidas.

1. **¿Qué categoría genera más ingresos?** Tecnología, con **14,290,000 unidades monetarias**. Criterio: suma de `total` agrupada por categoría; es el mayor ingreso.
2. **¿Qué canal vende más?** Online, con **35 ventas** frente a 33 de Tienda. Criterio: cantidad de transacciones. Online registró 14,669,000 y Tienda 4,507,000 unidades monetarias en ingresos.
3. **¿Los clientes VIP compran más que los Regulares?** Sí, en promedio por cliente. VIP: 29 compras entre 24 clientes (**1.2083 compras por cliente**) y 8,066,000 unidades monetarias de gasto total (**336,083.33 por cliente**). Regular: 39 compras entre 36 clientes (**1.0833 compras por cliente**) y 11,110,000 unidades monetarias de gasto total (**308,611.11 por cliente**). Se compararon promedios porque los segmentos tienen distinto número de clientes.
4. **¿Qué método de pago es el más usado?** Efectivo, con **30 ventas**; Tarjeta tuvo 25 y Transferencia 13. Criterio: conteo de ventas por método.
5. **¿Cuáles son los cinco clientes con más compras?** Hay empate con dos compras; se ordenó por gasto total como desempate:

   | Cliente | Compras | Gasto total |
   |---|---:|---:|
   | Nicolas Cardona | 2 | 2,515,000 |
   | Matias Rodriguez | 2 | 1,278,000 |
   | Mia Quintero | 2 | 1,090,000 |
   | Luna Montoya | 2 | 1,007,000 |
   | Luis Perez | 2 | 730,000 |

### Bonus: ingresos por mes

| Mes | Ingresos |
|---|---:|
| 2026-04 | 18,234,000 |
| 2026-05 | 942,000 |

Abril de 2026 tuvo más ingresos.

## Entregable 4: gráficos

Se generaron los dos gráficos de barras solicitados:

- [`images/ventas_por_categoria.png`](./images/ventas_por_categoria.png)
- [`images/ventas_por_canal.png`](./images/ventas_por_canal.png)

El código que los genera está en `graficos.py`; también se guardan bajo `Data/processed/graficos/`.

## Evidencias de terminal

Se incluyen capturas de ejecuciones reales en una terminal de PowerShell con el ambiente virtual del proyecto activo:

- [`images/00_ambiente_instalacion.png`](./images/00_ambiente_instalacion.png): ambiente virtual y dependencias.
- [`images/01_exploracion_clientes.png`](./images/01_exploracion_clientes.png) y [`images/01b_exploracion_ventas.png`](./images/01b_exploracion_ventas.png): `shape`, `info()` y `describe()` de los dos CSV originales.
- [`images/02_exploracion_script_parte1.png`](./images/02_exploracion_script_parte1.png), [`images/02_exploracion_script_parte2.png`](./images/02_exploracion_script_parte2.png), [`images/02_exploracion_script_parte3.png`](./images/02_exploracion_script_parte3.png), [`images/02_exploracion_script_parte4.png`](./images/02_exploracion_script_parte4.png) y [`images/02_exploracion_script_parte5.png`](./images/02_exploracion_script_parte5.png): salida completa de `exploracion.py`, dividida para que sea legible.
- [`images/03_limpieza.png`](./images/03_limpieza.png): nulos, duplicados, filas después de la limpieza y tipo de `fecha_venta`.
- [`images/04_validacion_merge.png`](./images/04_validacion_merge.png): validaciones y resultado de la unión.
- [`images/05_analisis_preguntas1_2.png`](./images/05_analisis_preguntas1_2.png) y [`images/05_analisis.png`](./images/05_analisis.png): resultados de las cinco preguntas y el bonus mensual.

Los gráficos del entregable 4 también están en `images/`: `ventas_por_categoria.png` y `ventas_por_canal.png`.
