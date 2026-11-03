from pathlib import Path

import matplotlib.pyplot as plt

SALIDA = Path(__file__).parent / "Data" / "processed" / "graficos"


def grafico_ventas_por_categoria(df):
    """Gráfico de barras: total vendido por categoría.

    Pistas:
    - Calcular datos = df.groupby("categoria")["total"].sum()
    - datos.plot(kind="bar") dibuja las barras.
    - plt.title, plt.xlabel y plt.ylabel ponen los textos.
    - plt.savefig(SALIDA / "ventas_por_categoria.png", bbox_inches="tight") guarda la imagen.
    - plt.show() la muestra en pantalla y plt.close() la cierra.
    """
    datos = df.groupby("categoria")["total"].sum()
    SALIDA.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(10, 6))
    datos.plot(kind="bar")
    plt.title("Ingresos por categoría")
    plt.xlabel("Categoría")
    plt.ylabel("Ingresos")
    plt.tight_layout()
    ruta = SALIDA / "ventas_por_categoria.png"
    plt.savefig(ruta, bbox_inches="tight")
    print(f"Gráfico guardado en: {ruta}")
    plt.show()
    plt.close()


def grafico_ventas_por_canal(df):
    """Gráfico de barras: total vendido por canal (Online contra Tienda).

    Usa los mismos pasos que la función anterior, cambiando la columna "categoria" por "canal".
    """
    datos = df.groupby("canal")["total"].sum()
    SALIDA.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 6))
    datos.plot(kind="bar")
    plt.title("Ingresos por canal")
    plt.xlabel("Canal")
    plt.ylabel("Ingresos")
    plt.tight_layout()
    ruta = SALIDA / "ventas_por_canal.png"
    plt.savefig(ruta, bbox_inches="tight")
    print(f"Gráfico guardado en: {ruta}")
    plt.show()
    plt.close()


def graficar(df):
    grafico_ventas_por_categoria(df)
    grafico_ventas_por_canal(df)
