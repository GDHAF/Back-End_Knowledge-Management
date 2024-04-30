import mysql.connector
from dao import Connection as conec

class ChatsUse:

    @staticmethod
    def Criar_Chat(nome_chat, desc):
        try:
            conec.Execute_Procedure("sp_new_chat", (nome_chat, desc))

        except mysql.connector.Error as error:
            print("Failed to execute stored procedure: {}".format(error))

    @staticmethod
    def Listar_Conversas(id_user):
        try:
            myresult = conec.Execute_Select("Call sp_listar_chats(%s)", list(id_user))

            return myresult

        except mysql.connector.Error as error:
            print("Failed to execute stored procedure: {}".format(error))

    @staticmethod
    def Entrar_Chat(nome):
        try:
            print("Chat")

        except mysql.connector.Error as error:
            print("Failed to execute stored procedure: {}".format(error))
