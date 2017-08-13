import sqlite3

def connect():
    conn=sqlite3.connect('creds.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS login (id INTEGER PRIMARY KEY,uname text,pword text)")
    conn.commit()
    conn.close()
    
def register(uname,pword):
    conn=sqlite3.connect('creds.db')
    cur=conn.cursor()
    cur.execute("INSERT INTO login VALUES (NULL,?,?)",(uname,pword))
    conn.commit()
    conn.close()
    
def search(name,passw):
    #print(name)
    #print(passw)
    conn=sqlite3.connect('creds.db')
    cur=conn.cursor()
    row=cur.execute("SELECT * FROM login WHERE uname=? and pword=?",(name,passw)).fetchall()
    if not row:
        conn.close()
        return False
    else:
        conn.close()
        return True
    