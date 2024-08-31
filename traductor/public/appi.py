from fastapi import FastAPI, Depends, HTTPException, status, Form
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

# Clave secreta para codificar los tokens JWT (debe mantenerse secreta en una aplicación real)
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Contexto de la contraseña para hash
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Base de datos falsa (en una aplicación real, usa una base de datos)
fake_users_db = {}

# Instancia de FastAPI
app = FastAPI()

# Instancia de OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Modelos
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

# Funciones de utilidad
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def create_user(db, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db[user.username] = {
        "username": user.username,
        "email": user.email,
        "full_name": None,
        "hashed_password": hashed_password,
        "disabled": False,
    }
    return UserInDB(**db[user.username])

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Endpoints

# Servir HTML para el formulario de registro
@app.get("/register_form/", response_class=HTMLResponse)
async def get_register_form():
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Registro de Usuario</title>
    </head>
    <body>
        <h2>Registro de Usuario</h2>
        <form action="/register_form/" method="post">
            <label for="username">Nombre de usuario:</label><br>
            <input type="text" id="username" name="username"><br><br>
            <label for="email">Correo electrónico:</label><br>
            <input type="email" id="email" name="email"><br><br>
            <label for="password">Contraseña:</label><br>
            <input type="password" id="password" name="password"><br><br>
            <input type="submit" value="Registrarse">
        </form>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

# Registro de usuarios desde el formulario
@app.post("/register_form/")
async def register_form(username: str = Form(...), email: str = Form(...), password: str = Form(...)):
    if username in fake_users_db:
        raise HTTPException(status_code=400, detail="El nombre de usuario ya está registrado")
    
    user = UserCreate(username=username, email=email, password=password)
    new_user = create_user(fake_users_db, user)
    return {"message": "Usuario registrado exitosamente", "user": new_user}

# Registro de usuarios con JSON
@app.post("/register/", response_model=User)
async def register(user: UserCreate):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="El nombre de usuario ya está registrado")
    
    new_user = create_user(fake_users_db, user)
    return new_user


