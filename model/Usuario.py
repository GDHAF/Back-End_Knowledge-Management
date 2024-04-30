class Usuario:

    def __init__(self, id_user, user, password, email, cargo):
        self._id = id_user
        self._user = user
        self._password = password
        self._email = email
        self._cargo = cargo

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    @property
    def pasword(self):
        return self._password

    @pasword.setter
    def pasword(self, password):
        self._pasword = password

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, cargo):
        self._cargo = cargo

