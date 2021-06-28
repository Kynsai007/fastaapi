import pyodbc,os


def getconnection():
    with pyodbc.connect(os.environ['SQLDBCONNECTIONSTRING']) as conn:
        return conn


def testconnection():
    try:
        connection = getconnection()
        return {'message':'Success'}
    except Exception as e:
        print(e)
        return {'message':'Failed'}

def getrecords():
    try:
        data = []
        connection = getconnection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * from azservices")
            for res in cursor:
                data.append({'Id':res[0],'Name':res[1],'Type':res[2],'Usage':res[3]})
        return {'message':'Success','data':data}
    except Exception as e:
        return {'message':'Exception','data':[]}