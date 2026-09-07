
import sqlite3
from pathlib import Path


# Pasta onde este arquivo está localizado
PASTA_ATUAL = Path(__file__).resolve().parent

# Arquivo do banco SQLite
BANCO = PASTA_ATUAL / "chamados.db"


def conectar():
    """Cria e retorna uma conexão com o banco de dados."""
    conexao = sqlite3.connect(BANCO)
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_tabela():
    """Cria a tabela chamados caso ela ainda não exista."""
    conexao = conectar()

    sql = """
    CREATE TABLE IF NOT EXISTS chamados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        descricao TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'aberto',
        criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        CHECK(status IN (
            'aberto',
            'em_andamento',
            'fechado'
        ))
    )
    """

    conexao.execute(sql)
    conexao.commit()
    conexao.close()


def inserir(titulo, descricao, status="aberto"):
    """Insere um novo chamado e retorna o ID gerado."""
    conexao = conectar()

    sql = """
    INSERT INTO chamados
    (titulo, descricao, status)
    VALUES (?, ?, ?)
    """

    cursor = conexao.execute(
        sql,
        (titulo, descricao, status)
    )

    conexao.commit()

    chamado_id = cursor.lastrowid

    conexao.close()

    return chamado_id


def listar():
    """Retorna todos os chamados."""
    conexao = conectar()

    sql = """
    SELECT id, titulo, descricao, status, criado_em
    FROM chamados
    ORDER BY id
    """

    dados = conexao.execute(sql).fetchall()

    conexao.close()

    return [dict(item) for item in dados]


def buscar_por_id(chamado_id):
    """Busca um chamado pelo ID."""
    conexao = conectar()

    sql = """
    SELECT id, titulo, descricao, status, criado_em
    FROM chamados
    WHERE id = ?
    """

    item = conexao.execute(
        sql,
        (chamado_id,)
    ).fetchone()

    conexao.close()

    if item is None:
        return None

    return dict(item)


def atualizar(chamado_id, titulo, descricao, status):
    """Atualiza um chamado existente."""
    conexao = conectar()

    sql = """
    UPDATE chamados
    SET titulo = ?, descricao = ?, status = ?
    WHERE id = ?
    """

    cursor = conexao.execute(
        sql,
        (titulo, descricao, status, chamado_id)
    )

    conexao.commit()

    alterados = cursor.rowcount

    conexao.close()

    return alterados


def excluir(chamado_id):
    """Exclui um chamado pelo ID."""
    conexao = conectar()

    sql = """
    DELETE FROM chamados
    WHERE id = ?
    """

    cursor = conexao.execute(
        sql,
        (chamado_id,)
    )

    conexao.commit()

    excluidos = cursor.rowcount

    conexao.close()

    return excluidos

