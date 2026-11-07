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
    # 1. Calcular los datos
    datos = df.groupby("categoria")["total"].sum().sort_values(ascending=False)

    # 2. Dibujar el gráfico
    plt.figure(figsize=(10, 6))
    datos.plot(kind="bar", color="skyblue", edgecolor="black")

    # 3. Personalización
    plt.title("Ingresos Totales por Categoría", fontsize=15)
    plt.xlabel("Categoría", fontsize=12)
    plt.ylabel("Total Vendido ($)", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # 4. Guardar y mostrar
    SALIDA.mkdir(parents=True, exist_ok=True)
    plt.savefig(SALIDA / "ventas_por_categoria.png", bbox_inches="tight")
    plt.show()
    plt.close()
    print(f"Gráfico guardado en: {SALIDA / 'ventas_por_categoria.png'}")


def grafico_ventas_por_canal(df):
    """Gráfico de barras: total vendido por canal (Online contra Tienda).

    Usa los mismos pasos que la función anterior, cambiando la columna "categoria" por "canal".
    """
    # 1. Calcular los datos
    datos = df.groupby("canal")["total"].sum().sort_values(ascending=False)

    # 2. Dibujar el gráfico
    plt.figure(figsize=(8, 6))
    datos.plot(kind="bar", color="salmon", edgecolor="black")

    # 3. Personalización
    plt.title("Ingresos Totales por Canal de Venta", fontsize=15)
    plt.xlabel("Canal", fontsize=12)
    plt.ylabel("Total Vendido ($)", fontsize=12)
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # 4. Guardar y mostrar
    SALIDA.mkdir(parents=True, exist_ok=True)
    plt.savefig(SALIDA / "ventas_por_canal.png", bbox_inches="tight")
    plt.show()
    plt.close()
    print(f"Gráfico guardado en: {SALIDA / 'ventas_por_canal.png'}")


def graficar(df):
    grafico_ventas_por_categoria(df)
    grafico_ventas_por_canal(df)
