from mysql.connector import connect

# Conectar com o banco de dados
conexao = connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'higors222'
)

cursor = conexao.cursor()
cursor.execute('SHOW DATABASES')

for i, database in enumerate(cursor, start=1):
    print(f'Banco de dados {i}: {database[0]}')


