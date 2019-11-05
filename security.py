from commons import log
import connexion
from connexion.exceptions import OAuthProblem

TOKEN_DB = {
    '123': {
        'uid': 0
    }
}
USER_DB = {
    'admin': {
        'passwd': '123'
    }
}

def basic_auth(username, password, required_scopes=None):
    log(username, password)
    log("Hi Security!")
    return True

def apikey_auth(token, required_scopes):
    validate = TOKEN_DB.get(token, None)
    if not validate:
        log('Invalid token','critical')
        raise OAuthProblem('Invalid token!')
    log(f'User Logged: {validate}')
    return validate