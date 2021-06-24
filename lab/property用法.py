class User(object):
    def __init__(self):
        self.password_hash = None

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = password

if __name__ == '__main__':
    u=User()
    u.password=123
    print(u.password_hash)
    print(u.password)
