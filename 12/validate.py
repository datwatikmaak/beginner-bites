from collections import namedtuple

User = namedtuple('User', 'name role expired')
USER, ADMIN = 'user', 'admin'
SECRET = 'I am a very secret token'

julian = User(name='Julian', role=USER, expired=False)
bob = User(name='Bob', role=USER, expired=True)
pybites = User(name='PyBites', role=ADMIN, expired=False)
USERS = (julian, bob, pybites)


# define exception classes here
class UserDoesNotExist(Exception):
    """Raise when the user doesnot exist """


class UserAccessExpired(Exception):
    """Raise when the user is expired"""


class UserNoPermission(Exception):
    """Raise when the user is not an admin"""


def get_secret_token(username):
    if username not in [user.name for user in USERS]:
        raise UserDoesNotExist("User does not exist", username)
    if username in [user.name for user in USERS if user.role == USER and not user.expired]:
        raise UserNoPermission("User does not have permission", username)
    if username in [user.name for user in USERS if user.role == USER and user.expired]:
        raise UserAccessExpired("User does not have access", username)
    if username in [user.name for user in USERS if user.role == ADMIN and not user.expired]:
        return SECRET
