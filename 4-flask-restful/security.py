from werkzeug.security import safe_str_cmp
from user import User

# Register user table
users = [
    User(1, 'sai', 'asdf'),
    User(2, 'joseph', 'joseph8888'),
]

# ----------- We don't needa iteraty our object table when we neeeda fetch the data -----------
username_table = {u.username: u for u in users} # {'user1': User(1, 'user1', 'abcxyz'), ....}
userid_table = {u.id: u for u in users} # {'2': User(2, 'user2', 'abcxyz'), ....}

# Step 1: User try to get a JWT token by requesting xxxx/auth, then we pass user info. to generate the JWT Token
def authenticate(username, password):
    user = username_table.get(username, None) # default value none.

    # safe string compare rather than user.password == password
    if user and safe_str_cmp(user.password, password):
        return user

# Step 2: This method uses to decode the JWT token user send us.
# Playload is the content of JWT token
def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)
