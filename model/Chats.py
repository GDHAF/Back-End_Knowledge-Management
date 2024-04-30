class Chats:
    def __init__(self, id_chat, nome_chat, data_cria, desc):
        self.id_chat = id_chat
        self.nome_chat = nome_chat
        self.data_cria = data_cria
        self.desc = desc

    @property
    def id_chat(self):
        return self.id_chat

    @id_chat.setter
    def id_chat(self, value):
        self._id_chat = value

    @property
    def nome_chat(self):
        return self.nome_chat

    @nome_chat.setter
    def nome_chat(self, value):
        self._nome_chat = value

    @property
    def data_cria(self):
        return self.data_cria

    @data_cria.setter
    def data_cria(self, value):
        self._data_cria = value

    @property
    def desc(self):
        return self.desc

    @desc.setter
    def desc(self, value):
        self._desc = value
