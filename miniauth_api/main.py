from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from miniauth_api.auth import register_user, authenticate_user
from miniauth_api.database import create_db_and_tables

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/register", response_class=HTMLResponse)
def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register")
def register(username: str = Form(...), password: str = Form(...)):
    register_user(username, password)
    return RedirectResponse("/", status_code=302)

@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    if authenticate_user(username, password):
        return {"message": "Login successful!"}
    return {"message": "Invalid credentials"}
