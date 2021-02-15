from server.model.user import User


def check_user_exist(user_name: str, password: str):
    return User.query.filter(User.user_name == user_name, User.password == password).first()
