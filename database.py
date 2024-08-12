# import sqlite3

# def init_db():
#     conn = sqlite3.connect('dictionary.db')
#     c = conn.cursor()
#     c.execute('''
#         CREATE TABLE IF NOT EXISTS terms (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             term TEXT NOT NULL,
#             definition TEXT NOT NULL
#         )
#     ''')
#     conn.commit()
#     conn.close()

# if __name__ == '__main__':
#     init_db()
