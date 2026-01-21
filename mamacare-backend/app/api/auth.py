from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.schemas.user_schema import UserCreate, UserLogin, Token, UserResponse
from app.core.security import get_password_hash, verify_password, create_access_token
from app.core.config import settings

router = APIRouter()

# This tells FastAPI that the token comes from the "/api/auth/login" endpoint
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

# --- MOCK DATABASE ---
fake_users_db = {}
user_id_counter = 1

def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    The Gatekeeper Function:
    1. Takes the token from the request header.
    2. Decodes it using the SECRET_KEY.
    3. If valid, returns the user info.
    4. If invalid, throws a 401 Unauthorized error.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        role: str = payload.get("role")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
        
    # In a real DB, we would fetch the full user object here.
    # For now, we return the data from the token payload.
    return {"email": email, "role": role}

@router.post("/signup", response_model=UserResponse)
def register_user(user_in: UserCreate):
    global user_id_counter
    if user_in.email in fake_users_db:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_pw = get_password_hash(user_in.password)
    new_user = {
        "id": user_id_counter,
        "email": user_in.email,
        "hashed_password": hashed_pw,
        "full_name": user_in.full_name,
        "role": user_in.role
    }
    fake_users_db[user_in.email] = new_user
    user_id_counter += 1
    return new_user

@router.post("/login", response_model=Token)
def login(user_in: UserLogin):
    user = fake_users_db.get(user_in.email)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    if not verify_password(user_in.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    access_token = create_access_token(subject=user["email"], role=user["role"])
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "role": user["role"],
        "user_name": user["full_name"]
    }