from cliente_dao import ClienteDAO
from cliente import Cliente

print('Clientes Zona Fit (GYM)')

opcion = None
while opcion != 5:
    print(f'''Menu:
          1. Listar Clientes
          2. Agregar Cliente
          3. Modificar Cliente
          4. Eliminar Cliente
          5. Salir
          '''),
    opcion = int(input('Elige tu opcion (1-5): '))
    if opcion == 1: # Listar clientes
        clientes = ClienteDAO.seleccionar()
        print('\n*** Listado de clientes ***')
        for cliente in clientes:
            print(cliente)
    elif opcion == 2: # Agregar cliente
        nombre_cliente = input('Escribe el nombre: ')
        apellido_cliente = input('Escribe el apellido: ')
        membresia_cliente = input('Escribe la membresia: ')
        cliente = Cliente(nombre=nombre_cliente, apellido=apellido_cliente, membresia=membresia_cliente)
        clientes_insertados = ClienteDAO.insertar(cliente)
        print(f'Clientes insertados: {clientes_insertados}')
    elif opcion == 3: # Modificar cliente
        id_cliente = int(input('Escribe el id del cliente a modificar: '))
        nombre_cliente = input('Escribe el nombre: ')
        apellido_cliente = input('Escribe el apellido: ')
        membresia_cliente = input('Escribe la membresia: ')
        cliente = Cliente(id_cliente, nombre_cliente, apellido_cliente, membresia_cliente)
        clientes_actualizados =ClienteDAO.actualizar(cliente)
        print(f'Clientes actualizados: {clientes_actualizados}')
    elif opcion == 4: # Eliminar cliente
        id_cliente = int(input('Escribe el id del cliente a eliminar: '))
        cliente = Cliente(id=id_cliente)
        clientes_eliminados = ClienteDAO.eliminar(cliente)
        print(f'Clientes eliminados: {clientes_eliminados}')
    else:
        print('Saliste de la aplicacion...')