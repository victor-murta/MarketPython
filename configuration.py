import os
import time
from typing import List
from  mysql.connector import Error
from main import *
import mysql.connector
import pyfiglet


def loginInDB():
    conexao = mysql.connector.connect(
        host= 'localhost',
        database='db_market',
        user='root',
        password= 'VmurtaG16',
    )
    try:    
        return conexao
    except Error as error:
        print('It hapenned an error: ', error)

connection = loginInDB()
cursor = connection.cursor()

def cursorLogOut(cursor):
    cursor.close()
    print('Cursor is closed')
    
def connectionLogOut(connection):
    connection.close()
    print('Connection is closed')

def Titulo():
    m = pyfiglet.figlet_format('MARKET')
    lines = '==='
    print(f'{lines}'*13)
    print(f'{m:>23}')
    print(f'{lines}'*13)

def Cart(list_cart):

    sql = '''SELECT * from tb_product '''
    cursor.execute(sql)
    lines = cursor.fetchall()

    lst = ['Id', 'Product name', 'Price', 'Qtd.']
    print(f'{lst[0]} {lst[1]:>15}       R$ {lst[2]} {lst[3]:>10}')   

    for product in list_cart:
        print(f'{product[0]} {product[1]:>20}       R$ {line[2]} {line[3]:>10}') 

def ListProducts():

    sql = '''SELECT * from tb_product '''
    cursor.execute(sql)
    lines = cursor.fetchall()

    lst = ['Id', 'Product name', 'Price', 'Qtd.']
    print(f'{lst[0]} {lst[1]:>15}       R$ {lst[2]} {lst[3]:>10}')   

    for line in lines:
        print(f'{line[0]} {line[1]:>20}       R$ {line[2]} {line[3]:>10}')   

def insertProduct():


    sql = f'''
        INSERT INTO tb_product
        ( productName, price, quantity)
        VALUES (%s, %s, %s)        
    '''

    name_product = input('Product name: ')
    price = input('Price: R$ ')
    quantity = input('Quantity: ')

    cursor.execute(sql, (name_product, price, quantity))
    connection.commit()

def ChangeProduct():
    Titulo()
    ListProducts()

    cng = input('''
Count: Salesman

    What change do yout want to do:
        [ 1 ] - Name
        [ 2 ] - Price
        [ 3 ] - Quantity
    ''')

    if cng == 1:
        sql = '''
        UPDATE tb_product 
        SET productName = %s
        WHERE id_product = %s
        '''

        id_product = input('Product id: ')
        name_product = input('New name: ')
    
        cursor.execute(sql, (id_product, name_product))
        connection.commit()

        

    elif cng == 2:
        sql = '''
        UPDATE tb_product 
        SET price = %s
        WHERE id_product = %s
        '''

        id_product = input('Product id: ')
        name_product = input('New price: R$ ')
        
        cursor.execute(sql, (id_product, name_product))
        connection.commit()

    elif cng == 3:
        sql = '''
        UPDATE tb_product 
        SET quantity = %s
        WHERE id_product = %s
        '''

        id_product = input('Product id: ')
        name_product = input('Quantity: ')
    
        cursor.execute(sql, (id_product, name_product))
        connection.commit()
        
    else:
        pass

def BuyProduct():
    ClearTerminal()
    Titulo()
    ListProducts()

    list_cart = []
    name_product = list_cart.append(input('Product name: '))
    id_product =  list_cart.append(input('Product id: '))
    quantity = list_cart.append(input('Quantity: '))

    cursor = connection.cursor()

    sql = '''SELECT * from tb_product '''
    cursor.execute(sql)
    list_product = cursor.fetchall()
    update_quantity = list_product[int(id_product) - 1][3] - int(quantity)    

    sql = '''
        UPDATE tb_product 
        SET quantity = %s
        WHERE productId = %s
    '''

    cursor.execute(sql, ( update_quantity ,id_product))
    connection.commit()


    return list_cart

def Choice():
    ClearTerminal()
    Titulo()

    while True:
        print('''
            [ 1 ] - Client
            [ 2 ] - Salesman
            [ 3 ] - Exit
        ''')
        i = int(input('Choose a number: '))
        if i == 1:
            ClearTerminal()
            Client()
        elif i == 2:
            ClearTerminal()
            Salesman()
        elif i == 3:
            time.sleep(1)
            print("Thanks to visit Murta's Market")
            break
        else:
            print("I didn't understand! ")

def ClearTerminal():
    os.system("cls")

def Client():
    ClearTerminal()
    Titulo()
    
    while True:

        print('''
    Count: Client

            [ 1 ] - View cart
            [ 2 ] - Buy
            [ 3 ] - Exit
            ''')

        i = int(input('Choose a number: '))    
        if i == 1:
            ClearTerminal()
            Titulo()
            ListProducts()
            break

        elif i == 2:
            Cart()

        elif i == 3 :
            time.sleep(1)
            print("Exiting as client ...")
            time.sleep(1)
            break
        else:
            print("I didn't understand! ")

def Salesman():
    ClearTerminal()
    Titulo()
    
    while True:
        print('''
    Count: Salesman

            [ 1 ] - Add product
            [ 2 ] - Edit product
            [ 3 ] - Buy
            [ 3 ] - View cart
            [ 5 ] - Exit
            ''')


        i = int(input('Choose a number: '))
        if i == 1:
            insertProduct()
            novo_produto = input('What to insert another product? (s/n)').strip().lower()

            if novo_produto == 'n':
                break

        elif i == 2:
            ChangeProduct()

            alterar_novamente = input('Wnat to change another product? (s/n)').strip().lower()

            if alterar_novamente == 'n':
                break

        elif i == 3:
            car = BuyProduct()
            Cart(car)

        elif i == 4:
            ListProducts()

        elif i == 5:
            time.sleep(1)
            print("Exiting as salesman...")
            break
        else:
            print("I didn't understand! ")

