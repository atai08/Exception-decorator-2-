
def decorator():
    def wrapper(*args):
        try:
            return func(*args)
        except:
            raise NameError('Exception: "No username defined!"')
    return wrapper

@decorator()
class User():
    def _init_(self, account):
        self.account = account
    
    def get_account_ballance(self):
        self.account = number + 2


u = User()
u.get_account_balance()