
class UserManager():
    user_name = ''
    def __init__(self, user_name):
        print(f'received data ata constructor --{user_name}')
        user_name = user_name

    @classmethod
    def set_user_name(cls, user_name_arg):
        print(f'data--{user_name_arg}')
        return cls(user_name_arg)

new_user = UserManager.set_user_name('asd')
print(new_user.user_name)
