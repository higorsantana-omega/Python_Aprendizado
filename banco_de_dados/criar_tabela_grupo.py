from bd import nova_conexao
from mysql.connector.errors import ProgrammingError

tabela_grupo = """
    CREATE TABLE grupo(
        id INT AUTO_INCREMENT PRIMARY KEY,
        descricao VARCHAR(40)
    )
"""

alterar_tabela_contato = """
    CREATE TABLE emails(
       ALTER TABLE contatos FOREIGN KEY (grupo_id),
       REFERENCES grupos(id)
    )
"""

alterar_tabela_contato_2 = """
    CREATE TABLE emails(
       ALTER TABLE contatos ADD grupo_id INT
    )
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(tabela_grupo)
        cursor.execute(alterar_tabela_contato_2)
        cursor.execute(alterar_tabela_contato)
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')