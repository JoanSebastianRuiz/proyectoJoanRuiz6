"""
    **Módulo de Gestión de Servicios:**

        - Operaciones CRUD para cada tipo de servicio ofrecido, como Internet de Fibra Óptica, planes pospago, prepago, etc.
        - Capacidad para agregar, modificar y eliminar servicios según sea necesario.
        - Registro de información detallada sobre cada servicio, incluyendo características, precios, entre otros.
"""
from validaciones import *

def agregar_servicio(datos):
    servicio={}
    bandera=False
    
    while bandera==False:
        codigo=input("Ingrese el codigo del servicio a agregar:")
        if validar_contiene_contenido(codigo)==True and validar_contiene_numeros(codigo)==True:
            bandera=True
    bandera=False
    
    if verificar_existencia_valor(datos,"codigo",codigo)==False:    
        servicio["codigo"]=codigo
        
        while bandera==False:
            nombre=input("Ingrese el nombre del servicio a agregar: ") 
            if validar_contiene_contenido(nombre)==True and validar_contiene_letras(nombre)==True:
                bandera=True
        bandera=False
        servicio["nombre"]= nombre
        
        while bandera==False:
            precio=input("Ingrese el precio del servicio a agregar: ")
            if validar_contiene_contenido(precio)==True and validar_contiene_numeros(precio)==True:
                bandera=True
        bandera=False
        servicio["precio"]=precio
        
        while bandera==False:
            caracteristicas=input("Ingrese las caracteristicas del servicio a agregar: ")
            if validar_contiene_contenido(caracteristicas)==True:
                bandera=True
        bandera=False
        servicio["caracteristicas"]=caracteristicas
        
        servicio["clientes"]=[]
        
        datos.append(servicio)
        print("El servicio se ha agregado correctamente")
        return datos
    
    else:
        print("El codigo ingresado ya se encuentra registrado en la lista de servicios")


def eliminar_servicio(datos):
    while bandera==False:
        codigo=input("Ingrese el codigo del servicio a eliminar:")
        if validar_contiene_contenido(codigo)==True and validar_contiene_numeros(codigo)==True:
            bandera=True
    bandera=False
    
    if verificar_existencia_valor(datos,"codigo",codigo)==True:
        diccionario=ubicacion_valor(datos,"codigo",codigo) 
        datos.remove(diccionario)
        print("El servicio se ha eliminado correctamente")
        return datos
    else:
        print("El codigo ingresado no se encuentra registrado en la lista de servicios")


def actualizar_servicio(datos):
    bandera=False
    while bandera==False:
        codigo=input("Ingrese el codigo del servicio a actualizar:")
        if validar_contiene_contenido(codigo)==True and validar_contiene_numeros(codigo)==True:
            bandera=True
    bandera=False
    
    if verificar_existencia_valor(datos,"codigo",codigo)==True:
        diccionario=ubicacion_valor(datos,"codigo",codigo)    
        diccionario["codigo"]=codigo
        
        while bandera==False:
            nombre=input("Ingrese el nombre del servicio a actualizar: ") 
            if validar_contiene_contenido(nombre)==True and validar_contiene_letras(nombre)==True:
                bandera=True
        bandera=False
        diccionario["nombre"]= nombre

        while bandera==False:
            precio=input("Ingrese el precio del servicio a actualizar: ")
            if validar_contiene_contenido(precio)==True and validar_contiene_numeros(precio)==True:
                bandera=True
        bandera=False
        diccionario["precio"]=precio

        while bandera==False:
            caracteristicas=input("Ingrese las caracteristicas del servicio a actualizar: ")
            if validar_contiene_contenido(caracteristicas)==True:
                bandera=True
        bandera=False
        diccionario["caracteristicas"]=caracteristicas
        
        print("El servicio se ha actualizado correctamente")
        return datos
    
    else:
        print("El codigo ingresado no se encuentra registrado en la lista de servicios")


def leer_servicios(datos):
    for diccionario in datos:
        for llave, valor in diccionario.items():
            if llave=="clientes":
                print(f"{llave}: ",end="")
                for i in range(len(valor)):
                    if i==len(valor)-1:
                        print(f"{valor[i]}")
                    else:
                        print(f"{valor[i]}, ", end="")
            else:
                print(f"{llave}: {valor}")
        print("")
