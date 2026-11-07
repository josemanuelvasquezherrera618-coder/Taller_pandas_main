# Taller práctico: análisis de datos con Pandas

**Nombre:** Jose Manuel Vásquez Herrera

## Negocios y respuestas

A continuación se presentan los resultados del análisis de negocio, resaltando los elementos con mejor desempeño en cada ámbito:

### 1. Categoría con Mayor Desempeño (Ingresos)
| Categoría | Desempeño | Criterio |
| :--- | :--- | :--- |
| **Top Categoría** | Genera la mayor suma de ingresos totales | `df.groupby("categoria")["total"].sum().idxmax()` |

### 2. Canal de Ventas más Eficiente
| Canal | Resultado | Criterio |
| :--- | :--- | :--- |
| **Canal Líder** | Mayor volumen de ventas en ingresos | `df.groupby("canal")["total"].sum().idxmax()` |

### 3. Comparativa de Segmentos de Clientes
| Segmento | Desempeño por Cliente | Criterio |
| :--- | :--- | :--- |
| **VIP vs Regular** | Se determina quién gasta más en promedio por persona | `Gasto Total / Clientes Únicos` |

### 4. Método de Pago Preferido
| Método de Pago | Uso | Criterio |
| :--- | :--- | :--- |
| **Más Utilizado** | Mayor frecuencia de transacciones | `df["metodo_pago"].value_counts().idxmax()` |

### 5. Top 5 Clientes con Mejor Desempeño
| Ranking | Cliente | Métrica de Éxito |
| :--- | :--- | :--- |
| **Top 1 al 5** | Los clientes con más compras totales | `sort_values(by=["cantidad_compras", "gasto_total"])` |
