from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database import Base, engine, SessionLocal
from backend.models.user import User
from backend.schemas import UserCreate, UserLogin, Token
from backend.auth import hash_password, verify_password, create_access_token
from backend.dependencies import get_current_user

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Secure Financial API")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/signup", response_model=Token)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        email=user.email,
        hashed_password=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    token = create_access_token({"sub": new_user.id})
    return {"access_token": token}


@app.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": db_user.id})
    return {"access_token": token}


@app.get("/secure-data")
def secure_endpoint(user_id: int = Depends(get_current_user)):
    return {
        "message": "Access granted",
        "user_id": user_id
    }
