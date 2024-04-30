class Postagem:
    def __init__(self, id_post, texto, data_post, n_up, id_doc, id_user):
        self.id_post = id_post
        self.texto = texto
        self.data_post = data_post
        self.n_up = n_up
        self.id_doc = id_doc
        self.id_user = id_user

    @property
    def id_post(self):
        return self.id_post

    @id_post.setter
    def id_post(self, value):
        self.id_post = value

    @property
    def texto(self):
        return self.texto

    @texto.setter
    def texto(self, value):
        self.texto = value

    @property
    def data_post(self):
        return self.data_post

    @data_post.setter
    def data_post(self, value):
        self.data_post = value

    @property
    def n_up(self):
        return self.n_up

    @n_up.setter
    def n_up(self, value):
        self.n_up = value

    @property
    def id_doc(self):
        return self.id_doc

    @id_doc.setter
    def id_doc(self, value):
        self.id_doc = value

    @property
    def id_user(self):
        return self.id_user

    @id_user.setter
    def id_user(self, value):
        self.id_user = value
