from conexion import Conexion
from cliente import Cliente

class ClienteDAO:
    SELECCIONAR = 'SELECT * FROM cliente ORDER BY id'
    INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES (%s, %s, %s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'
    
    @classmethod
    def seleccionar(cls):
        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            clientes = []
            for registro in registros:
                cliente = Cliente(registro['id'], registro['nombre'], registro['apellido'], registro['membresia'])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'Ocurrió un error al seleccionar clientes: {e}')
        finally:
            if cursor:
                cursor.close()
            if conexion:
                Conexion.liberar_conexion(conexion)
                
    @classmethod
    def insertar(cls, cliente):
        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al insertar un cliente: {e}')
        finally:
            if cursor:
                cursor.close()
            if conexion:
                Conexion.liberar_conexion(conexion)
                
    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al actualizar un cliente: {e}')
        finally:
            if cursor:
                cursor.close()
            if conexion:
                Conexion.liberar_conexion(conexion)
                
    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al eliminar un cliente: {e}')
        finally:
            if cursor:
                cursor.close()
            if conexion:
                Conexion.liberar_conexion(conexion)
        

if __name__ == '__main__':
    
    # Seleccionar clientes
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)
