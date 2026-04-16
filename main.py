import funciones
import datetime

listaProductos=funciones.leerArchivo("productos.json")
listaMesas=funciones.leerArchivo("mesas.json")
listaClientes=funciones.leerArchivo("clientes.json")
listaFacturas = funciones.leerArchivo("factura.json")

while True:
    funciones.menuPrincipal()
    opcionPrincipal = input("Digite la opcion: ")
    print("---------------------------------------")

    if opcionPrincipal == "1":
        while True:
            funciones.menuProductos()
            opcionProductos = int(input("Digite la opcion: "))
            print("---------------------------------------")
            if(opcionProductos==1):
                listaProductos = funciones.registrarProductos(listaProductos)
                    
            elif(opcionProductos==2):
                for producto in listaProductos:
                    print(producto)
            elif(opcionProductos==3):
                "saliendo...."
                break

    elif opcionPrincipal == "2":
        while True:
            funciones.menuMesas()
            opcionMesas = int(input("Digite la opcion: "))
            print("---------------------------------------")
            if(opcionMesas==1):
                funciones.registrarMesas(listaMesas)
                    
            elif(opcionMesas==2):
                for mesas in listaMesas:
                    print(mesas)
            elif(opcionMesas==3):
                "saliendo...."
                break
    
    elif opcionPrincipal == "3":
        while True:
            funciones.menuClientes()
            opcionClientes = int(input("Digite la opcion: "))
            print("---------------------------------------")
            if(opcionClientes==1):
                diccionarioClientes= {
                    "identificacion":input("digite identificacion: "),
                    "nombre":input("digite nombre: "),
                    "telefono":input("digite telefono: ")
                }
                listaClientes.append(diccionarioClientes)
                funciones.guardarArchivo("clientes.json",listaClientes)
                    
            elif(opcionClientes==2):
                for clientes in listaClientes:
                    print(clientes)
            elif(opcionClientes==3):
                "saliendo...."
                break
    elif opcionPrincipal == "4":
        listaFactura = funciones.leerArchivo("factura.json")
        
        listaProductosFactura = []
        print("facturacion")
        codigoMesa= input("digite codigo de la mesa: ")
        cliente= input("digite identificacion del cliente: ")
        
        while True:
            codigoProducto= input("digite codigo del producto: ")
            for producto in listaProductos:
                if(producto["codigo"]==codigoProducto):
                    cantidad= input("digite cantidad: ")
                    productoFactura= {
                        "codigo": codigoProducto,
                        "cantidad": cantidad
                    }
                    listaProductosFactura.append(productoFactura)
                    break 
            
            opcionFactura= input("quieres agregar mas productos s/n: ")
            if(opcionFactura=="n"):
                break
        
        diccionarioFactura={
            "fecha": datetime.datetime.now().strftime("%Y-%m-%d"),
            "cliente": cliente,
            "codigoMesa": codigoMesa,
            "productos": listaProductosFactura
        }
        
        print("----------Factura----------")
        print(f"Fecha: {diccionarioFactura['fecha']}")
        print(f"Cliente: {diccionarioFactura['cliente']}")
        print(f"Codigo Mesa: {diccionarioFactura['codigoMesa']}")
        print(f"Productos: {diccionarioFactura['productos']}")
        
        listaFactura.append(diccionarioFactura)
        funciones.guardarArchivo("factura.json", listaFactura)
    elif opcionPrincipal == "5":
        print("--- REPORTE DE VENTAS POR FECHA ---")
        fecha_inicio = input("Digite fecha de inicio (AAAA-MM-DD): ")
        fecha_fin = input("Digite fecha de fin (AAAA-MM-DD): ")
        
        todas_las_facturas = funciones.leerArchivo("factura.json")
        
        facturas_seleccionadas = []
        
        for factura in todas_las_facturas:
            if fecha_inicio <= factura["fecha"] <= fecha_fin:
                facturas_seleccionadas.append(factura)
        
        if len(facturas_seleccionadas) == 0:
            print("No se encontraron facturas en ese rango de fechas.")
        else:
            funciones.generarReporteCSV(facturas_seleccionadas, listaProductos)
    elif opcionPrincipal == "6":
        print("Analizando datos de ventas...")
        fecha_inicio = input("Digite fecha de inicio (AAAA-MM-DD): ")
        fecha_fin = input("Digite fecha de fin (AAAA-MM-DD): ")
        funciones.reporteElMasVendido(fecha_inicio, fecha_fin)
    elif opcionPrincipal == "7":
        print("Saliendo del sistema...")
        break
    else:
        print("Opcion no valida")
