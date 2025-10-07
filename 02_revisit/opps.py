
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

