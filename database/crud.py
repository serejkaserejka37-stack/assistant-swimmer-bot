from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from .models import Base, User, Analysis
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_user(telegram_id, first_name=None, username=None):
    db = next(get_db())
    user = User(telegram_id=telegram_id, first_name=first_name, username=username)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_telegram_id(telegram_id):
    db = next(get_db())
    return db.query(User).filter(User.telegram_id == telegram_id).first()
