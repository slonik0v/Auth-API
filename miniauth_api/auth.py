from passlib.context import CryptContext
from miniauth_api.models import User
from miniauth_api.database import session

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def register_user(username: str, password: str):
    hashed = pwd_context.hash(password)
    user = User(username=username, password_hash=hashed)
    session.add(user)
    session.commit()

def authenticate_user(username: str, password: str):
    user = session.query(User).filter(User.username == username).first()
    if user and pwd_context.verify(password, user.password_hash):
        return True
    return False
