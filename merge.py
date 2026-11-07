from pathlib import Path

PROCESSED = Path(__file__).parent / "Data" / "processed"


def validar_premerge(clientes, ventas):
    """Revisa que el merge se pueda hacer. Devuelve True si todo está bien, False si no.

    Revisar:
    - Que exista la columna "id_cliente" en los dos dataframes.
    - Que "id_cliente" no esté repetido en clientes.
    - Que "id_cliente" tenga el mismo tipo en los dos dataframes.
    - Cuántas ventas no tienen cliente asociado (esto solo se informa, no falla).
    """
    # 1. Verificar que la columna exista en ambos
    if "id_cliente" not in clientes.columns or "id_cliente" not in ventas.columns:
        print("Error: La columna 'id_cliente' no existe en una de las tablas.")
        return False

    # 2. Verificar que no haya IDs repetidos en la tabla de clientes
    if clientes["id_cliente"].duplicated().any():
        print("Error: Hay IDs de cliente duplicados en la tabla de clientes.")
        return False

    # 3. Verificar que el tipo de dato sea el mismo
    if clientes["id_cliente"].dtype != ventas["id_cliente"].dtype:
        print(f"Error: Tipos de datos incompatibles. Clientes: {clientes['id_cliente'].dtype}, Ventas: {ventas['id_cliente'].dtype}")
        return False

    # 4. Informar sobre ventas sin cliente (esto no hace que la función devuelva False)
    ventas_sin_cliente = ventas[~ventas["id_cliente"].isin(clientes["id_cliente"])].shape[0]
    print(f"Información: Hay {ventas_sin_cliente} ventas sin un cliente asociado en la tabla de clientes.")

    return True


def unir(clientes, ventas):
    """Une ventas con clientes usando "id_cliente" y guarda el resultado en Data/processed/merge.csv.

    Pistas:
    - Usar pd.merge(...) o ventas.merge(...).
    - Usar how="left" para no perder ventas.
    - Usar validate="m:1" para confirmar que cada venta tiene un solo cliente.
    - Guardar con df.to_csv(...) en PROCESSED / "merge.csv".
    """
    # 1. Ejecutar la validación previa
    if not validar_premerge(clientes, ventas):
        print("Error: No se pudo realizar la unión debido a fallos en la validación.")
        return None

    # 2. Realizar el merge
    # how="left" asegura que no perdamos ninguna fila de la tabla de ventas
    # validate="m:1" confirma que el id_cliente es único en la tabla de clientes
    df_merge = ventas.merge(clientes, on="id_cliente", how="left", validate="m:1")

    # 3. Guardar el resultado en la carpeta de procesados
    PROCESSED.mkdir(parents=True, exist_ok=True) # Asegura que la carpeta exista
    df_merge.to_csv(PROCESSED / "merge.csv", index=False)
    print(f"Éxito: Tabla unida guardada en {PROCESSED / 'merge.csv'}")

    return df_merge
