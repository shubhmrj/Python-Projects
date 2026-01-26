from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import models, database, auth
from .models import User, Project
import os
import subprocess

app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/signup")
def signup(username: str, password: str, db: Session = Depends(get_db)):
    if db.query(User).filter(User.username == username).first():
        raise HTTPException(status_code=400, detail="Username already registered")
    user = User(username=username, hashed_password=auth.get_password_hash(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"msg": "User created"}

@app.post("/token")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = auth.authenticate_user(db, username, password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    token = auth.create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/projects")
def list_projects(db: Session = Depends(get_db), user: User = Depends(auth.get_current_user)):
    return db.query(Project).all()

@app.get("/project/{project_id}")
def get_project(project_id: int, db: Session = Depends(get_db), user: User = Depends(auth.get_current_user)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    with open(f"backend/projects/{project.filename}", "r") as f:
        code = f.read()
    return {"name": project.name, "description": project.description, "code": code}

@app.post("/run/{project_id}")
def run_project(project_id: int, db: Session = Depends(get_db), user: User = Depends(auth.get_current_user)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    try:
        result = subprocess.run(["python", f"backend/projects/{project.filename}"], capture_output=True, text=True, timeout=10)
        return {"stdout": result.stdout, "stderr": result.stderr}
    except Exception as e:
        return {"stdout": "", "stderr": str(e)}
