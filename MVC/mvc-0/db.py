import sqlite3


def _executar(query, params=None):
    """Executa consultas no banco SQLite, aplicando commit em operacoes de escrita."""
    db_path = "./geek.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    resultado = None

    try:
        cursor.execute(query, params or [])
        if query.lstrip().upper().startswith("SELECT"):
            resultado = cursor.fetchall()
        else:
            conn.commit()
            resultado = cursor.rowcount
    except Exception as e:
        print(f"Erro ao executar a query: {e}")
    finally:
        conn.close()

    return resultado if resultado is not None else []
