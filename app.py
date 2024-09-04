from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from esrogimDb import EsrogimDB




app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

db = EsrogimDB("db")




@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "esrogim": db.get_all_available_esrogim()})

@app.get("/initiate-reservation/{esrog_id}")
async def initiate_reservation(request: Request, esrog_id: int):
    result: tuple[str] = db.check_reserved(esrog_id)
    is_reserved = result[0]
    if is_reserved != '__not_reserved__':
        return {"message": "already reserved"}
    
    return {"message": "this esrog is not reserved yet please enter your name to reserve it"}


@app.put("/reserve/{esrog_id}/{username}")
async def reserve(request: Request, esrog_id: int, username: str):
    if db.reserve_esrog(esrog_id, username):
        return {"message": "this esrog is now reserved for you until the end of the day, please come by the store to pick it up"}
    
    return {"message": "reservation failed"}

