import mysql.connector

import model.Postagem
import dao.Connection as conec


class Comentarios:

    @staticmethod
    def Comentar(texto, id_user, id_post):

        try:

            conec.Execute_Procedure("sp_comentar_post", (texto, id_user, id_post))

            print("Postado com êxito.")
        except mysql.connector.Error as error:
            print("Failed to execute stored procedure: {}".format(error))
        except:
            print("Erro ao fazer postagem.")

    @staticmethod
    def Listar_Comments(id_post):
        try:
            i = [id_post]
            myresult = conec.Execute_Select("Call sp_listar_comments(%s)", i)

            return myresult
        except mysql.connector.Error as error:
            print("Failed to execute stored procedure: {}".format(error))
        except:
            print("Erro ao Listar Comentários.")
