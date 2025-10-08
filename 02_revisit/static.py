
class UserManager:
    def __init__(self):
        pass
    
    @staticmethod
    def get_user_name():
        print('this is a static method, no need of self argument')

UserManager.get_user_name()

