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


def ingresos_por_categoria(df):
    """Pregunta 1: ¿Qué categoría genera más ingresos?

    Pista: df.groupby("categoria")["total"].sum().sort_values(ascending=False)
    """
    # Calcular ingresos por categoría
    ingresos = df.groupby("categoria")["total"].sum().sort_values(ascending=False)

    categoria_top = ingresos.idxmax() # Obtiene el nombre de la categoría con el valor máximo
    monto_top = ingresos.max()

    print("\n--- Ingresos por Categoría ---")
    print(ingresos)
    print(f"\nLa categoría que más genera ingresos es: {categoria_top} con ${monto_top:,.2f}")


def canal_que_mas_vende(df):
    """Pregunta 2: ¿Qué canal vende más?

    Pista: agrupar por "canal" y usar .agg(ventas=("id_venta", "count"), ingresos=("total", "sum")).
    """
    # Calcular ventas y totales por canal
    resumen_canal = df.groupby("canal").agg(
        ventas=("id_venta", "count"),
        ingresos=("total", "sum")
    )

    canal_top_ingresos = resumen_canal["ingresos"].idxmax()
    monto_top = resumen_canal["ingresos"].max()

    print("\n--- Ventas por Canal ---")
    print(resumen_canal)
    print(f"\nEl canal que más vende (en ingresos) es: {canal_top_ingresos} con ${monto_top:,.2f}")


def clientes_vip_vs_regular(df):
    """Pregunta 3: ¿Los clientes VIP compran más que los Regulares?

    Pista: como hay más clientes Regular que VIP, compare promedios por cliente, no totales.
    Calcular: número de clientes (nunique), compras y gasto total por segmento,
    y luego dividir compras y gasto entre el número de clientes.
    """
    # 1. Calcular totales y conteos por segmento
    # Usamos nunique para contar clientes únicos en cada segmento
    resumen_segmento = df.groupby("segmento_cliente").agg(
        num_clientes=("id_cliente", "nunique"),
        total_compras=("id_venta", "count"),
        gasto_total=("total", "sum")
    )

    # 2. Calcular promedios por cliente
    resumen_segmento["promedio_compras"] = resumen_segmento["total_compras"] / resumen_segmento["num_clientes"]
    resumen_segmento["promedio_gasto"] = resumen_segmento["gasto_total"] / resumen_segmento["num_clientes"]

    print("\n--- Comparativa Segmentos (Promedios por Cliente) ---")
    print(resumen_segmento)

    # Determinar quién gasta más en promedio
    ganador = resumen_segmento["promedio_gasto"].idxmax()
    print(f"\nEn promedio, los clientes {ganador} gastan más por persona.")


def metodo_pago_mas_usado(df):
    """Pregunta 4: ¿Qué método de pago es más usado?

    Pista: df["metodo_pago"].value_counts()
    """
    # Contar frecuencias de cada método de pago
    conteo_pagos = df["metodo_pago"].value_counts()

    metodo_top = conteo_pagos.idxmax()
    cantidad_top = conteo_pagos.max()

    print("\n--- Uso de Métodos de Pago ---")
    print(conteo_pagos)
    print(f"\nEl método de pago más usado es: {metodo_top} con {cantidad_top} transacciones.")


def top5_clientes(df):
    """Pregunta 5: ¿Top 5 clientes con más compras?

    Pista: agrupar por ["id_cliente", "nombre_cliente"], contar compras y sumar total,
    ordenar por compras (y por gasto como desempate) y tomar las primeras 5 con .head(5).
    """
    # Agrupar por cliente y calcular métricas
    top_clientes = df.groupby(["id_cliente", "nombre_cliente"]).agg(
        cantidad_compras=("id_venta", "count"),
        gasto_total=("total", "sum")
    )

    # Ordenar por cantidad de compras (descendente) y luego por gasto (descendente)
    top_clientes = top_clientes.sort_values(
        by=["cantidad_compras", "gasto_total"],
        ascending=False
    ).head(5)

    print("\n--- Top 5 Clientes con más compras ---")
    print(top_clientes)
