from bd import nova_conexao

sql = "SELECT id, nome, tel FROM contatos WHERE nome like '%h%'"

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    for x in cursor:
        print(x)
