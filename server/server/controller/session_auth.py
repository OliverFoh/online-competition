from functools import wraps
from flask import session

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # if g.user is None:
        #     return redirect(url_for('login', next=request.url))
        if 'account' in session:
            pass
        else:
            print('请先登录')
            return {'status': True, 'is_login': False, 'msg':'You do not have permission'}
        return f(*args, **kwargs)
    return decorated_function