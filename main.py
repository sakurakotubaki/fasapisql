# main.py
from fastapi import FastAPI, Request  # RequestをFastAPIからインポート
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

# 静的ファイルのマウント
app.mount("/static", StaticFiles(directory="static"), name="static")

# テンプレートの設定
templates = Jinja2Templates(directory="templates")

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        name="item.html",
        context={
            "request": request,  # requestは必須
            "id": id
        }
    )

# ルートパスのハンドラも追加
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        name="home.html",
        context={
            "request": request
        }
    )