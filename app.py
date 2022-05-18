import os
import ibm_db
import pandas as pd
from flask import Flask
app = Flask(__name__)

conn=ibm_db.connect(os.environ['dbcred'], "", "")

@app.route("/")

@app.route('/db2')
def access_db():
    try:
        sql = ''' SELECT * FROM JDIRVING.DEMAND '''
        df = pd.read_sql(sql, conn)
        #dictionary = ibm_db.fetch_both(stmt)
        if(df):
            return "<h1 style='text-align:center;'>Table Values</br></h1>"\
                    +f"<h2 style='color:blue;text-align:center;'></br>{df['Volume'][0]}</h2>"
        else:
            return "<h1 style='color:red;text-align:center;'>Table Values Is Empty"
            
    except:
        return "<h1 style='color:red;text-align:center;'>Table Values Doesn't Exist"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
