from flask import Flask, render_template, request
from fpreprocesamiento import controller
import json

app = Flask(__name__, static_folder='static', static_url_path='/static')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def dashboard_route():
    mas_solicitados = controller.mas_solicitados()
    return render_template('index.html',mas_solicitados=mas_solicitados)

@app.route('/tables-solicitados.html')
def tables_route():
    mas_solicitados = controller.mas_solicitados()
    mas_solicitados = mas_solicitados.to_json(orient='records')
    mas_solicitados = json.loads(mas_solicitados)
    
    menos_solicitados = controller.menos_solicitados()
    menos_solicitados = menos_solicitados.to_json(orient='records')
    menos_solicitados = json.loads(menos_solicitados)
    
    return render_template(
        'tables-solicitados.html', 
        mas_solicitados = mas_solicitados, 
        menos_solicitados=menos_solicitados
        )
    
@app.route('/tables-vendidos.html')
def tables_vendidos_route():
    mas_vendidos = controller.mas_vendidos()
    mas_vendidos = mas_vendidos.to_json(orient='records')
    mas_vendidos = json.loads(mas_vendidos)
    
    menos_vendidos = controller.menos_vendidos()
    menos_vendidos = menos_vendidos.to_json(orient='records')
    menos_vendidos = json.loads(menos_vendidos)
    
    return render_template(
        'tables-vendidos.html', 
        mas_vendidos = mas_vendidos, 
        menos_vendidos = menos_vendidos
        )

@app.route('/table-pedidos-cliente.html')
def table_pedidos_cliente():
    pedidos_cliente = controller.pedidos_cliente()
    pedidos_cliente = pedidos_cliente.to_json(orient='records')
    pedidos_cliente = json.loads(pedidos_cliente)
    
    return render_template(
        'table-pedidos-cliente.html', 
        pedidos_cliente = pedidos_cliente, 
        )

@app.route('/table-pedidos-mes.html')
def table_pedidos_xmes():
    pedidos_xmes = controller.pedidos_xmes()
    pedidos_xmes = pedidos_xmes.to_json(orient='records')
    pedidos_xmes = json.loads(pedidos_xmes)
    
    return render_template(
        'table-pedidos-mes.html', 
        pedidos_xmes = pedidos_xmes, 
        )

@app.route('/tables-pedidos-pago-anio.html')
def table_pedidos_xpago():
    pedidos_pago = controller.pedidos_xforma_pago()
    pedidos_pago = pedidos_pago.to_json(orient='records')
    pedidos_pago = json.loads(pedidos_pago)
    
    pedidos_año = controller.pedidos_xaño()
    pedidos_año = pedidos_año.to_json(orient='records')
    pedidos_año = json.loads(pedidos_año)
    
    return render_template(
        'tables-pedidos-pago-anio.html', 
        pedidos_pago = pedidos_pago, 
        pedidos_año = pedidos_año, 
        )
    
@app.route('/table-productos-categoria.html')
def table_productos_xcategoria():
    productos_categoria = controller.productos_xcategoria()
    productos_categoria = productos_categoria.to_json(orient='records')
    productos_categoria = json.loads(productos_categoria)
    
    return render_template(
        'table-productos-categoria.html', 
        productos_categoria = productos_categoria, 
        )

@app.route('/table-ventas-empleado.html')
def table_ventas_por_empleado():
    ventas_empleado = controller.ventas_por_empleado_2021()
    ventas_empleado = ventas_empleado.to_json(orient='records')
    ventas_empleado = json.loads(ventas_empleado)
    
    return render_template(
        'table-ventas-empleado.html', 
        ventas_empleado = ventas_empleado, 
        )

@app.route('/table-ventas-cliente.html')
def table_ventas_por_cliente():
    ventas_cliente = controller.ventas_totales_por_cliente()
    ventas_cliente = ventas_cliente.to_json(orient='records')
    ventas_cliente = json.loads(ventas_cliente)
    
    return render_template(
        'table-ventas-cliente.html', 
        ventas_cliente = ventas_cliente, 
        )



@app.route('/charts.html')
def chart_route():
    mas_solicitados = controller.mas_solicitados()
    mas_solicitados = mas_solicitados.to_json(orient='records')
    mas_solicitados = json.loads(mas_solicitados)
    
    menos_solicitados = controller.menos_solicitados()
    menos_solicitados = menos_solicitados.to_json(orient='records')
    menos_solicitados = json.loads(menos_solicitados)
    
    mas_vendidos = controller.mas_vendidos()
    mas_vendidos = mas_vendidos.to_json(orient='records')
    mas_vendidos = json.loads(mas_vendidos)
    
    menos_vendidos = controller.menos_solicitados()
    menos_vendidos = menos_vendidos.to_json(orient='records')
    menos_vendidos = json.loads(menos_vendidos)
    
    pedidos_cliente = controller.pedidos_cliente()
    pedidos_cliente = pedidos_cliente.to_json(orient='records')
    pedidos_cliente = json.loads(pedidos_cliente)
    
    pedidos_xmes = controller.pedidos_xmes()
    pedidos_xmes = pedidos_xmes.to_json(orient='records')
    pedidos_xmes = json.loads(pedidos_xmes)
    
    pedidos_pago = controller.pedidos_xforma_pago()
    pedidos_pago = pedidos_pago.to_json(orient='records')
    pedidos_pago = json.loads(pedidos_pago)
    
    pedidos_año = controller.pedidos_xaño()
    pedidos_año = pedidos_año.to_json(orient='records')
    pedidos_año = json.loads(pedidos_año)
    
    productos_categoria = controller.productos_xcategoria()
    productos_categoria = productos_categoria.to_json(orient='records')
    productos_categoria = json.loads(productos_categoria)
    
    ventas_empleado = controller.ventas_por_empleado_2021()
    ventas_empleado = ventas_empleado.to_json(orient='records')
    ventas_empleado = json.loads(ventas_empleado)
    
    ventas_cliente = controller.ventas_totales_por_cliente()
    ventas_cliente = ventas_cliente.to_json(orient='records')
    ventas_cliente = json.loads(ventas_cliente)
    
    return render_template(
        'charts.html',
        methods=['GET'],
        mas_solicitados = mas_solicitados,
        menos_solicitados = menos_solicitados,
        mas_vendidos = mas_vendidos,
        menos_vendidos = menos_vendidos,
        pedidos_cliente = pedidos_cliente,
        pedidos_xmes = pedidos_xmes,
        pedidos_pago = pedidos_pago,
        pedidos_año = pedidos_año,
        productos_categoria = productos_categoria,
        ventas_empleado = ventas_empleado,
        ventas_cliente = ventas_cliente,
        )
    

@app.route('/get-massolicitados', methods=['GET'])
def get_data():
    mas_solicitados = controller.mas_solicitados()
    mas_solicitados = mas_solicitados.to_json(orient='records')
    mas_solicitados = json.loads(mas_solicitados)
    return json.loads(mas_solicitados)
if __name__ == '__main__':
    app.run(debug=True)