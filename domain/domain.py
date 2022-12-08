from api import api


def login_flow(host, account, password):
    flag, message = api.login(host, account, password)
    if not flag:
        return False
    flag, message = api.launch(host)
    if not flag:
        return False
    return True
