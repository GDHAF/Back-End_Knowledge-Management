import mysql.connector


def Connection():
    """

    :rtype: mysql.connector.cursor()
    """
    mydb = mysql.connector.connect(
        host="localhost",
        user="henri",
        password="123456",
        database="Conhecimento"
    )

    return mydb


def Execute_Select(proc, val):
    try:
        mydb = Connection()
        mycursor = mydb.cursor()

        mycursor.execute(proc, val)
        retorno = mycursor.fetchall()

        mycursor.close()

        return retorno
    except mysql.connector.Error as error:
        print("Failed to execute stored procedure: {}".format(error))


def Execute_Procedure(proc, val):
    try:
        mydb = Connection()
        mycursor = mydb.cursor()

        var = mycursor.callproc(proc, val)

        mydb.commit()

        mycursor.close()

        return var
    except mysql.connector.Error as error:
        print("Failed to execute stored procedure: {}".format(error))
