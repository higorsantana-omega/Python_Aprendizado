from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = (
    ('Higor', '963367427'),
    ('João', '9633632427'),
    ('Gabriel', '962127427'),
    ('Alessandro', '96336437'),
    ('Ronaldo', '963367421')
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'Foram incluidos {cursor.lastrowid} no registro!')