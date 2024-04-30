import mysql.connector
from dao import Connection as conec
import controller.Text_Analyser as analys

class Postagem_Use:

    @staticmethod
    def Postar(texto, id_user):

        try:

            tags = analys.Analyser.Create_Base(texto)
            id_ptg = 0

            id_post = conec.Execute_Procedure("sp_new_post", (texto, id_user, id_ptg))

            for i in tags:
                conec.Execute_Procedure("sp_tag_creation", (i, id_post[2]))

            print("Postado com êxito.")
        except mysql.connector.Error as error:
            print("Failed to execute stored procedure: {}".format(error))
        except:
            print("Erro ao fazer postagem.")

    @staticmethod
    def Listar_Posts():
        try:

            myresult = conec.Execute_Select("Call sp_listar_posts", None)
            return myresult
        except mysql.connector.Error as error:
            print("Failed to execute stored procedure: {}".format(error))
        except:
            print("Erro ao cadastrar usuário.")
