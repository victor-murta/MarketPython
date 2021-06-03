from mysql.connector import connection
import configuration as config


connection = config.loginInDB()
cursor = connection.cursor() # where I run my sql commands


config.Titulo()
config.Choice()

config.connectionLogOut(connection)
config.cursorLogOut(cursor)

