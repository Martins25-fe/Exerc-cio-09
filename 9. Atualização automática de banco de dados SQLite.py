import sqlite3
import pandas as pd

# Conectando ao banco de dados SQLite (se o banco não existir, ele será criado)
conn = sqlite3.connect('vendas.db')
cursor = conn.cursor()

# Lendo o arquivo CSV usando pandas
csv_file = 'dados_vendas.csv'
df = pd.read_csv(csv_file)

# Criando a tabela no banco de dados (caso não exista)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto TEXT,
        quantidade INTEGER,
        preco REAL,
        data_venda TEXT
    )
''')

# Inserindo os dados do CSV na tabela 'vendas'
for index, row in df.iterrows():
    cursor.execute('''
        INSERT INTO vendas (produto, quantidade, preco, data_venda)
        VALUES (?, ?, ?, ?)
    ''', (row['produto'], row['quantidade'], row['preco'], row['data_venda']))

# Commitando as mudanças e fechando a conexão
conn.commit()

# Fechando a conexão
conn.close()









