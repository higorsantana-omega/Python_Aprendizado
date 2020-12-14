from bd import nova_conexao

sql = 'SELECT id, nome FROM contatos ORDER BY nome ASC'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    print('\n'.join(str(registro) for registro in cursor))