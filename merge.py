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
    validacion_correcta = True
    columnas_requeridas = "id_cliente"
    columnas_faltantes = [
        nombre
        for nombre, df in (("clientes", clientes), ("ventas", ventas))
        if columnas_requeridas not in df.columns
    ]

    if columnas_faltantes:
        print(
            "[merge] Falta la columna 'id_cliente' en: "
            + ", ".join(columnas_faltantes)
        )
        validacion_correcta = False

    if columnas_faltantes:
        return False

    duplicados = clientes["id_cliente"].duplicated().sum()
    if duplicados:
        print(
            f"[merge] Error: hay {duplicados} valores de id_cliente duplicados "
            "en clientes."
        )
        validacion_correcta = False
    else:
        print("[merge] OK: id_cliente no está duplicado en clientes.")

    tipo_clientes = clientes["id_cliente"].dtype
    tipo_ventas = ventas["id_cliente"].dtype
    if tipo_clientes != tipo_ventas:
        print(
            "[merge] Error: id_cliente tiene tipos distintos "
            f"(clientes: {tipo_clientes}; ventas: {tipo_ventas})."
        )
        validacion_correcta = False
    else:
        print(f"[merge] OK: id_cliente tiene el mismo tipo ({tipo_clientes}).")

    ventas_sin_cliente = ~ventas["id_cliente"].isin(clientes["id_cliente"])
    cantidad_sin_cliente = int(ventas_sin_cliente.sum())
    print(
        f"[merge] Ventas sin cliente asociado: {cantidad_sin_cliente} "
        "(se conservarán con el merge left)."
    )

    return validacion_correcta


def unir(clientes, ventas):
    """Une ventas con clientes usando "id_cliente" y guarda el resultado en Data/processed/merge.csv.

    Pistas:
    - Usar pd.merge(...) o ventas.merge(...).
    - Usar how="left" para no perder ventas.
    - Usar validate="m:1" para confirmar que cada venta tiene un solo cliente.
    - Guardar con df.to_csv(...) en PROCESSED / "merge.csv".
    """
    if not validar_premerge(clientes, ventas):
        print("[merge] No se realizó la unión porque falló una validación.")
        return None

    df_merge = ventas.merge(
        clientes,
        on="id_cliente",
        how="left",
        validate="m:1",
    )
    PROCESSED.mkdir(parents=True, exist_ok=True)
    ruta_salida = PROCESSED / "merge.csv"
    df_merge.to_csv(ruta_salida, index=False)

    print(f"[merge] Unión completada: {df_merge.shape[0]} filas y {df_merge.shape[1]} columnas.")
    print(f"[merge] Archivo guardado en: {ruta_salida}")
    return df_merge
