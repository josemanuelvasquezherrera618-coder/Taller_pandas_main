# Taller práctico: análisis de datos con Pandas

**Nombre:** Jose Manuel Vásquez Herrera

## Negocios y respuestas

| Pregunta | Respuesta | Criterio / Lógica aplicada |
|---|---|---|
| **1. ¿Qué categoría genera más ingresos?** | Se identifica la categoría con la suma más alta de la columna `total`. | `df.groupby("categoria")["total"].sum().sort_values(ascending=False)` |
| **2. ¿Qué canal vende más?** | Se identifica el canal con el mayor monto total de ingresos. | `df.groupby("canal").agg(ingresos=("total", "sum")).idxmax()` |
| **3. ¿Los clientes VIP compran más que los Regulares?** | Se comparan los promedios de gasto y compras por cliente único en cada segmento. | `Total de gasto / Número de clientes únicos (nunique)` |
| **4. ¿Qué método de pago es el más usado?** | Se cuenta la frecuencia de aparición de cada método de pago. | `df["metodo_pago"].value_counts().idxmax()` |
| **5. ¿Cuáles son los cinco clientes con más compras?** | Se agrupa por cliente, se cuenta el número de ventas y se ordena descendentemente. | `df.groupby(["id_cliente", "nombre_cliente"]).count().sort_values(by="id_venta", ascending=False).head(5)` |
