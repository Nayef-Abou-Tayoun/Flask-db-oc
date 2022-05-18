import os
import ibm_db
from flask import Flask
app = Flask(__name__)

conn=ibm_db.connect(os.environ['dbcred'], "", "")

@app.route("/")

@app.route('/db2')
def access_db():
    try:
        sql = ''' SELECT * FROM JDIRVING.DEMAND '''
        stmt = ibm_db.exec_immediate(conn,sql)
        dictionary = ibm_db.fetch_both(stmt)
        if(dictionary):
            return "<h1 style='text-align:center;'>Table Values</br></h1>"\
                    +f"<h2 style='color:blue;text-align:center;'></br>{dictionary['NAME']}</h2>"
        else:
            return "<h1 style='color:red;text-align:center;'>Table Values Is Empty"
            
    except:
        return "<h1 style='color:red;text-align:center;'>Table Values Doesn't Exist"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
