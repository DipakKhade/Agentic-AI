
class UserManager:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
    
    def get_user(self):
        return {
            'user_id': self.user_id,
            'user_name': self.user_name
        }
    

new_user = UserManager(user_id=1, user_name='Dipak')
print(new_user.get_user())


class AdminManager(UserManager):
    def __init__(self, user_id, user_name):
        super().__init__(user_id, user_name)
    

new_admin = AdminManager(2, 'Gaurav')
print(new_admin.get_user())


class A:
    def __init__(self):
        pass

    def a_method(self):
        print('printing from class A')

class B:
    a_instane = A

    def __init__(self):
        self.b = self.a_instane()
    
    def b_method(self):
        self.b.a_method()

b = B()
b.b_method()


class C(A, B):
    def __init__(self):
        super().__init__()