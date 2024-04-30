class Tags:
    def __init__(self, id_Tag, nome_Tag):
        self._id_tag = id_Tag
        self._nome_tag = nome_Tag

    @property
    def id_tag(self):
        return self._id_tag

    @id_tag.setter
    def id_tag(self, id_tag):
        self._id_tag = id_tag

    @property
    def nome_tag(self):
        return self._nome_tag

    @nome_tag.setter
    def nome_tag(self, nome_tag):
        self._nome_tag = nome_tag
