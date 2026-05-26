# ============================================================
#   UNAD - Fundamentos de Programación (213022)
#   Fase 5 – Evaluación Final POA
#   Problema 3: Auditoría de Inventario
# ============================================================
#
#   Lógica de negocio:
#     • Si stock_actual < stock_minimo  →  pedir = minimo - actual
#     • Si stock_actual >= stock_minimo →  pedir = 0
# ============================================================


# ------------------------------------------------------------------
# DATOS INICIALES – matriz con 5 artículos
# Formato: [Código, Nombre, Stock Actual, Stock Mínimo Requerido]
# ------------------------------------------------------------------
inventario = [
    ["A001", "Cuadernos universitarios",  8,  15],
    ["A002", "Bolígrafos azules",         20,  20],
    ["A003", "Resmas de papel carta",      2,  10],
    ["A004", "Carpetas archivadoras",     12,   5],
    ["A005", "Marcadores permanentes",     0,   8],
]


# ------------------------------------------------------------------
# MÓDULO / FUNCIÓN PRINCIPAL
# ------------------------------------------------------------------
def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """
    Determina cuántas unidades de un artículo deben pedirse.

    Parámetros:
        stock_actual  (int): Unidades disponibles en bodega.
        stock_minimo  (int): Nivel mínimo requerido del artículo.

    Retorna:
        int: Cantidad a pedir (0 si el stock es suficiente).
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0


# ------------------------------------------------------------------
# FUNCIÓN DE REPORTE
# ------------------------------------------------------------------
def generar_informe_pedidos(matriz_inventario):
    """
    Recorre la matriz de inventario, calcula cuánto pedir por artículo
    e imprime el informe de pedidos.

    Parámetros:
        matriz_inventario (list): Matriz con filas
                                  [código, nombre, actual, mínimo].
    """
    print("=" * 55)
    print("       INFORME DE AUDITORÍA DE INVENTARIO")
    print("=" * 55)
    print(f"{'Artículo':<30} {'A pedir':>10}")
    print("-" * 55)

    articulos_a_pedir = 0

    for fila in matriz_inventario:
        codigo      = fila[0]
        nombre      = fila[1]
        actual      = fila[2]
        minimo      = fila[3]

        cantidad = calcular_cantidad_a_pedir(actual, minimo)

        if cantidad > 0:
            estado = f"{cantidad} unidades  ⚠ REABASTECER"
            articulos_a_pedir += 1
        else:
            estado = "No requiere pedido  ✔"

        print(f"[{codigo}] {nombre:<26} {estado}")

    print("-" * 55)
    print(f"Total de artículos que requieren reabastecimiento: "
          f"{articulos_a_pedir}")
    print("=" * 55)


# ------------------------------------------------------------------
# PUNTO DE ENTRADA
# ------------------------------------------------------------------
if __name__ == "__main__":
    generar_informe_pedidos(inventario)
