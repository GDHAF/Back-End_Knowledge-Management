import mysql.connector


# -------------------------------------------------------------------------------



class Mensagem:
    def __init__(self, id_Msg, data_envio, texto, id_user, id_chat):
        self.id_Msg = id_Msg
        self.data_envio = data_envio
        self.texto = texto
        self.id_user = id_user
        self.id_chat = id_chat


# --------------------------------------------


class Documents:
    def __init__(self, id_Doc, nome_Arc, path, tipo_Ext):
        self.id_Doc = id_Doc
        self.nome_Arc = nome_Arc
        self.path = path
        self.tipo_Ext = tipo_Ext
