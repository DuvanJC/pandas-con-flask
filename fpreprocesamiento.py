import pandas as pd 
from flask import jsonify

class Preprocesamiento: 
    def leer_categorias():
        categorias_df = pd.read_csv("categorias.csv", sep=';', encoding='UTF-8')
        return categorias_df
    
    def leer_clientes():
        clientes_df = pd.read_csv("clientes.csv", sep=';', encoding='UTF-8')
        return clientes_df
    
    def leer_departments():
        departments_df = pd.read_csv("departments.csv", sep=';', encoding='UTF-8')
        return departments_df
    
    def leer_detalles_pedidos():
        detalles_pedidos_df = pd.read_csv("detalles_pedidos.csv", sep=';', encoding='UTF-8')
        return detalles_pedidos_df
    
    def leer_employees():
        df_emp = pd.read_csv("employees_m.csv", sep=';', encoding='UTF-8')
        return df_emp
    
    def leer_pedidos():
        pedidos_df = pd.read_csv("pedidos.csv", sep=';', encoding='UTF-8')
        return pedidos_df

    def leer_productos():
        productos_df = pd.read_csv("productos.csv", sep=';', encoding='UTF-8')
        return productos_df
    
class controller:
    # def __init__(self):
    #     self.preprocesamiento = Preprocecamiento()
    
    def mas_solicitados():
        productos_df = Preprocesamiento.leer_productos()
        detalles_pedidos_df = Preprocesamiento.leer_detalles_pedidos()
        productos_con_cantidad = detalles_pedidos_df.merge(productos_df, on='Id_Producto')
        productos_con_cantidad_agrupados = productos_con_cantidad.groupby('Nombre_Producto')['Id_Producto'].count().reset_index(name='Cantidad')
        productos_con_cantidad_agrupados_ordenados = productos_con_cantidad_agrupados.sort_values(by='Cantidad', ascending=False)
        productos_con_cantidad_agrupados_ordenados = productos_con_cantidad_agrupados_ordenados.head(10)
        return productos_con_cantidad_agrupados_ordenados
    

    def menos_solicitados():
        productos_df = Preprocesamiento.leer_productos()
        detalles_pedidos_df = Preprocesamiento.leer_detalles_pedidos()
        productos_con_cantidad = detalles_pedidos_df.merge(productos_df, on='Id_Producto')
        productos_con_cantidad_agrupados = productos_con_cantidad.groupby('Nombre_Producto')['Id_Producto'].count().reset_index(name='Cantidad')
        productos_con_cantidad_agrupados_ordenados = productos_con_cantidad_agrupados.sort_values(by='Cantidad', ascending=True)
        productos_con_cantidad_agrupados_ordenados = productos_con_cantidad_agrupados_ordenados.head(10)
        return productos_con_cantidad_agrupados_ordenados


    def mas_vendidos():
        productos_df = Preprocesamiento.leer_productos()
        detalles_pedidos_df = Preprocesamiento.leer_detalles_pedidos()
        productos_con_cantidad = detalles_pedidos_df.merge(productos_df, on='Id_Producto')
        productos_con_cantidad_agrupados = productos_con_cantidad.groupby('Nombre_Producto')['Id_Producto'].sum().reset_index(name='Cantidad')
        productos_con_cantidad_agrupados_ordenados = productos_con_cantidad_agrupados.sort_values(by='Cantidad', ascending=False)
        productos_con_cantidad_agrupados_ordenados = productos_con_cantidad_agrupados_ordenados.head(10)
        return productos_con_cantidad_agrupados_ordenados
    
    def menos_vendidos():
        productos_df = Preprocesamiento.leer_productos()
        detalles_pedidos_df = Preprocesamiento.leer_detalles_pedidos()
        productos_con_cantidad = detalles_pedidos_df.merge(productos_df, on='Id_Producto')
        productos_con_cantidad_agrupados = productos_con_cantidad.groupby('Nombre_Producto')['Id_Producto'].sum().reset_index(name='Cantidad')
        productos_con_cantidad_agrupados_ordenados = productos_con_cantidad_agrupados.sort_values(by='Cantidad', ascending=True)
        productos_con_cantidad_agrupados_ordenados = productos_con_cantidad_agrupados_ordenados.head(10)
        return productos_con_cantidad_agrupados_ordenados


    def pedidos_cliente():
        pedidos_df = Preprocesamiento.leer_pedidos()
        clientes_df = Preprocesamiento.leer_clientes()
        pedidos_con_clientes_df = pedidos_df.merge(clientes_df, on="Id_Cliente")
        pedidos_por_cliente_df = pedidos_con_clientes_df.groupby('Nombre_Compañia')['Id_Cliente'].count().reset_index()
        pedidos_por_cliente_df.rename(columns={'Nombre_Compañia': 'Nombre_Cliente', 'Id_Cliente': 'Cantidad_Pedidos'}, inplace=True)
        pedidos_por_cliente_df = pedidos_por_cliente_df.sort_values(by='Cantidad_Pedidos', ascending=False)
        pedidos_por_cliente_df = pedidos_por_cliente_df.head(10)
        productos = pedidos_por_cliente_df[['Nombre_Cliente', 'Cantidad_Pedidos']]
        return productos

    def pedidos_xmes():
        pedidos_df = Preprocesamiento.leer_pedidos()
        pedidos_df['Mes_Pedido'] = pd.to_datetime(pedidos_df['Fecha_Pedido']).dt.month_name()
        pedidos_por_mes_df = pedidos_df.groupby('Mes_Pedido')['Id_Pedido'].count().reset_index()
        pedidos_por_mes_df.rename(columns={'Id_Pedido': 'Cantidad_Pedidos'}, inplace=True)
        pedidos_por_mes_df = pedidos_por_mes_df.sort_values(by='Mes_Pedido')
        productos = pedidos_por_mes_df[['Mes_Pedido', 'Cantidad_Pedidos']]
        return productos


    def pedidos_xforma_pago():
        pedidos_df = Preprocesamiento.leer_pedidos()
        pedidos_por_forma_pago_df = pedidos_df.groupby('Forma_Pago')['Id_Pedido'].count().reset_index()
        pedidos_por_forma_pago_df.rename(columns={'Id_Pedido': 'Cantidad_Pedidos'}, inplace=True)
        pedidos_por_forma_pago_df = pedidos_por_forma_pago_df.sort_values(by='Forma_Pago')
        pedidos_por_forma_pago = pedidos_por_forma_pago_df[['Forma_Pago', 'Cantidad_Pedidos']]
        return pedidos_por_forma_pago


    def pedidos_xaño():
        pedidos_df = Preprocesamiento.leer_pedidos()
        pedidos_df['Anio'] = pd.to_datetime(pedidos_df['Fecha_Pedido']).dt.year
        pedidos_por_año_df = pedidos_df.groupby('Anio')['Id_Pedido'].count().reset_index()
        pedidos_por_año_df.rename(columns={'Id_Pedido': 'Cantidad_Pedidos'}, inplace=True)
        pedidos_por_año_df = pedidos_por_año_df.sort_values(by='Anio')
        pedidos_por_año = pedidos_por_año_df[['Anio', 'Cantidad_Pedidos']]
        return pedidos_por_año


    def productos_xcategoria():
        productos_df = Preprocesamiento.leer_productos()
        categorias_df = Preprocesamiento.leer_categorias()
        productos_con_categoria_df = productos_df.merge(categorias_df, on='Id_Categoria')
        productos_por_categoria_df = productos_con_categoria_df.groupby('Nombre_Categoria')['Id_Producto'].count().reset_index()
        productos_por_categoria_df.rename(columns={'Id_Producto': 'Cantidad_Productos'}, inplace=True)
        productos_por_categoria_df = productos_por_categoria_df.sort_values(by='Cantidad_Productos', ascending=False)
        return productos_por_categoria_df


    def ventas_por_empleado_2021():
        pedidos_df = Preprocesamiento.leer_pedidos()
        empleados_df = Preprocesamiento.leer_employees()
        pedidos_2021_df = pedidos_df[pd.to_datetime(pedidos_df['Fecha_Pedido']).dt.year == 2021]
        ventas_por_empleado_2021_df = pedidos_2021_df.groupby('EMPLOYEE_ID')['Id_Pedido'].count().reset_index()
        ventas_por_empleado_2021_df = ventas_por_empleado_2021_df.merge(empleados_df, on='EMPLOYEE_ID')
        ventas_por_empleado_2021_df.rename(columns={'Id_Pedido': 'VENTAS_2021'}, inplace=True)
        ventas_por_empleado_2021_df = ventas_por_empleado_2021_df.sort_values(by='VENTAS_2021', ascending=False)
        return ventas_por_empleado_2021_df

    def ventas_totales_por_cliente():
        pedidos_df = Preprocesamiento.leer_pedidos()
        productos_df = Preprocesamiento.leer_productos()
        detalles_pedidos_df = Preprocesamiento.leer_detalles_pedidos()
        pedidos_con_detalles_df = pedidos_df.merge(detalles_pedidos_df, on='Id_Pedido')
        pedidos_con_detalles_productos_df = pedidos_con_detalles_df.merge(productos_df, on='Id_Producto')
        pedidos_con_detalles_productos_df['TOTAL_PEDIDO'] = pedidos_con_detalles_productos_df['Precio_por_Unidad'] * pedidos_con_detalles_productos_df['Cantidad']
        ventas_totales_por_cliente_df = pedidos_con_detalles_productos_df.groupby('Id_Cliente')['TOTAL_PEDIDO'].sum().reset_index()
        return ventas_totales_por_cliente_df
    