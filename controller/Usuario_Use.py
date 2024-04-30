import mysql.connector
from dao import Connection as conec


class UsuarioUse:

    @staticmethod
    def login(val):
        try:

            myresult = conec.Execute_Select('Call sp_login(%s, %s)', (val[0], val[1]))

            if myresult.__len__() > 0:
                print(f"Bem vindo, {myresult[0][1]}.")

                return myresult[0]
            else:
                print("Usuário não encontrado")

        except mysql.connector.Error as error:
            print("Failed to execute stored procedure: {}".format(error))

    @staticmethod
    def sign_Up(nome, senha, email, carreira):
        try:

            conec.Execute_Procedure('sp_sign_up', (nome, senha, email, carreira))

            print(f"Usuário {nome} foi cadastrado com sucesso.")

        except:
            print("Erro ao cadastrar usuário.")

    @staticmethod
    def Update_User(id, senha, carreira):

        try:
            conec.Execute_Procedure("sp_update_user", (id, senha, carreira))

            print("Usuário atualizado com sucesso.")

        except:
            print("Erro ao cadastrar usuário.")
