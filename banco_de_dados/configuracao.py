from mysql.connector import connect

# Conectar com o banco de dados
conexao = connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'higors222'
)

print(conexao)
