import json
import csv
import datetime
def menuPrincipal():
    print("---------------------------------------")
    print("SISTEMA DE FACRURACION RESTAURANTE ACME")
    print("1. Menu productos")
    print("2. Menu mesas")
    print("3. Menu clientes")
    print("4. Crear factura")
    print("5. Registro de ventas")
    print("6. Reporte del producto mas vendido")
    print("7. Salir")
    print("---------------------------------------")
    
def menuProductos():
    print("---------------------------------------")
    print("MENU PRODUCTOS")
    print("1. registrar producto")
    print("2. ver productos")
    print("3. Salir")
    print("---------------------------------------")
    
def menuMesas():
    print("---------------------------------------")
    print("MENU MESAS")
    print("1. registrar mesas")
    print("2. ver mesas")
    print("3. Salir")
    print("---------------------------------------")
    
def menuClientes():
    print("---------------------------------------")
    print("MENU CLIENTES")
    print("1. registrar clientes")
    print("2. ver clientes")
    print("3. Salir")
    print("---------------------------------------")

def leerArchivo(ruta):
    try:
        with open(ruta,"r")as file:
            return json.load(file)
    except Exception:
        return []
    
def guardarArchivo(ruta,datos):
    with open(ruta,"w")as file:
        json.dump(datos,file,indent=4)
    

def registrarProductos(listaProductos):
    diccionarioProductos = {
        "codigo":input("digite codigo: "),
        "nombre":input("digite nombre: "),
        "precio":input("digite precio: "),
        "iva":input("digite iva: ")
    }
    listaProductos.append(diccionarioProductos)
    guardarArchivo("productos.json",listaProductos)
    return listaProductos
    
def registrarMesas(listaMesas):
    diccionarioMesas = {
        "codigo":input("digite codigo: "),
        "nombre":input("digite nombre: "),
        "puestos":input("digite puestos: "),
    }
    listaMesas.append(diccionarioMesas)
    guardarArchivo("mesas.json",listaMesas)
    return listaMesas

def generarReporteCSV(facturasFiltradas, listaProductos):
    nombre_archivo = "reporte_ventas.csv"
    encabezados = ["Mesa", "Producto", "Cantidad", "Subtotal", "IVA", "Total"]
    
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(encabezados) 

        for factura in facturasFiltradas:
            mesa = factura["codigoMesa"]
            
            for item in factura["productos"]:
                for p in listaProductos:
                    if p["codigo"] == item["codigo"]:
                        precio = float(p["precio"])
                        iva_porc = float(p["iva"])
                        cant = int(item["cantidad"])
                        
                        subtotal = precio * cant
                        iva_valor = subtotal * iva_porc
                        total = subtotal + iva_valor
                        
                        writer.writerow([mesa, p["nombre"], cant, subtotal, iva_valor, total])
    
    print("---------------------------------------")
    print(f"¡Listo! Archivo '{nombre_archivo}' creado.")
    print("---------------------------------------")

        
def reporteElMasVendido(INICIO, FIN):
    todas_las_facturas = leerArchivo("factura.json")    
    facturas_seleccionadas = []
    for factura in todas_las_facturas:
        if INICIO <= factura["fecha"] <= FIN:
            facturas_seleccionadas.append(factura)
    if len(facturas_seleccionadas) == 0:
        print("No se encontraron facturas en ese rango de fechas.")   
    else:
        listaFacturas = leerArchivo("factura.json")
        listaProductos= leerArchivo("productos.json")
        conteo_reporte = []
        for p in listaProductos:
                diccionario_auxiliar = {
                "codigo": str(p["codigo"]),"nombre" : str(p["nombre"]),
                "vendidos": 0          
                }
                conteo_reporte.append(diccionario_auxiliar)
        for factura in listaFacturas:
            for item in factura["productos"]:
                codigo_vendido = str(item["codigo"]) 
                cantidad_vendida = int(item["cantidad"])
                
                for producto_conteo in conteo_reporte:
                    if producto_conteo["codigo"] == codigo_vendido:
                        producto_conteo["vendidos"] = producto_conteo["vendidos"] + cantidad_vendida
                        break 
        lista_ordenada = sorted(conteo_reporte, key= lambda x: x["vendidos"])
        print("\n---------- El Producto mas vendido  ----------")
        print (lista_ordenada[-1])
        acceso = (lista_ordenada[-1])
        acceso["Fecha"]= datetime.datetime.now().strftime("%Y-%m-%d")
        guardarArchivo("ElMasVendido.json",acceso)
        print("-------------------------------------------------------")
    