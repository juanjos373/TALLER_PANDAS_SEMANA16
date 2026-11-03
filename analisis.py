import pandas as pd

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)


def analizar(df):
    print("\nInfo general:")
    df.info()
    print("\nEstadísticas numéricas:")
    print(df.describe())

    ingresos_por_categoria(df)
    canal_que_mas_vende(df)
    clientes_vip_vs_regular(df)
    metodo_pago_mas_usado(df)
    top5_clientes(df)
    ventas_por_mes(df)


def ingresos_por_categoria(df):
    """Pregunta 1: ¿Qué categoría genera más ingresos?

    Pista: df.groupby("categoria")["total"].sum().sort_values(ascending=False)
    """
    ingresos = df.groupby("categoria")["total"].sum().sort_values(ascending=False)
    print("\nIngresos por categoría:")
    print(ingresos.to_string())
    if not ingresos.empty:
        print(f"Categoría con más ingresos: {ingresos.index[0]} ({ingresos.iloc[0]:,.0f}).")
    return ingresos


def canal_que_mas_vende(df):
    """Pregunta 2: ¿Qué canal vende más?

    Pista: agrupar por "canal" y usar .agg(ventas=("id_venta", "count"), ingresos=("total", "sum")).
    """
    resumen = (
        df.groupby("canal")
        .agg(ventas=("id_venta", "count"), ingresos=("total", "sum"))
        .sort_values("ventas", ascending=False)
    )
    print("\nVentas e ingresos por canal:")
    print(resumen.to_string())
    if not resumen.empty:
        canal_lider = resumen["ventas"].idxmax()
        print(
            f"Canal con más ventas (criterio: cantidad de transacciones): "
            f"{canal_lider} ({resumen.loc[canal_lider, 'ventas']} ventas)."
        )
    return resumen


def clientes_vip_vs_regular(df):
    """Pregunta 3: ¿Los clientes VIP compran más que los Regulares?

    Pista: como hay más clientes Regular que VIP, compare promedios por cliente, no totales.
    Calcular: número de clientes (nunique), compras y gasto total por segmento,
    y luego dividir compras y gasto entre el número de clientes.
    """
    resumen = (
        df.groupby("segmento_cliente")
        .agg(
            clientes=("id_cliente", "nunique"),
            compras=("id_venta", "count"),
            gasto_total=("total", "sum"),
        )
    )
    resumen["compras_por_cliente"] = resumen["compras"] / resumen["clientes"]
    resumen["gasto_por_cliente"] = resumen["gasto_total"] / resumen["clientes"]
    print("\nComparación por segmento (promedios por cliente):")
    print(resumen.to_string())
    return resumen


def metodo_pago_mas_usado(df):
    """Pregunta 4: ¿Qué método de pago es más usado?

    Pista: df["metodo_pago"].value_counts()
    """
    conteos = df["metodo_pago"].value_counts()
    print("\nVentas por método de pago:")
    print(conteos.to_string())
    if not conteos.empty:
        mas_usados = conteos[conteos == conteos.max()].index.tolist()
        print(
            "Método(s) más usado(s): "
            f"{', '.join(map(str, mas_usados))} ({conteos.max()} ventas)."
        )
    return conteos


def top5_clientes(df):
    """Pregunta 5: ¿Top 5 clientes con más compras?

    Pista: agrupar por ["id_cliente", "nombre_cliente"], contar compras y sumar total,
    ordenar por compras (y por gasto como desempate) y tomar las primeras 5 con .head(5).
    """
    top = (
        df.groupby(["id_cliente", "nombre_cliente"])
        .agg(
            compras=("id_venta", "count"),
            gasto_total=("total", "sum"),
        )
        .sort_values(["compras", "gasto_total"], ascending=[False, False])
        .head(5)
    )
    print("\nTop 5 clientes por compras (gasto total como desempate):")
    print(top.to_string())
    return top


def ventas_por_mes(df):
    """Bonus: suma las ventas por mes calendario (año y mes)."""
    resumen = (
        df.assign(mes=df["fecha_venta"].dt.to_period("M"))
        .groupby("mes")["total"]
        .sum()
        .sort_values(ascending=False)
    )
    print("\nIngresos por mes:")
    print(resumen.to_string())
    if not resumen.empty:
        print(
            f"Mes con más ingresos: {resumen.index[0]} "
            f"({resumen.iloc[0]:,.0f})."
        )
    return resumen
