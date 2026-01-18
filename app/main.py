from dotenv import load_dotenv
load_dotenv()

from pydantic import BaseModel
from fastapi import FastAPI, UploadFile, Request, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from PyPDF2 import PdfReader

from app.ai_service import classify_email_with_ai, generate_response


app = FastAPI(title="Email AI Classifier")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# =========================
# MODELO DE ENTRADA
# =========================
class EmailRequest(BaseModel):
    content: str


def read_email_file(file: UploadFile) -> str:
    if file.filename.endswith(".txt"):
        return file.file.read().decode("utf-8")

    if file.filename.endswith(".pdf"):
        reader = PdfReader(file.file)
        return "".join(page.extract_text() or "" for page in reader.pages)

    return ""


# =========================
# ROTAS
# =========================
@app.post("/classify-email")
def classify_email(email: EmailRequest):
    try:
        category = classify_email_with_ai(email.content)
        response = generate_response(category, email.content)

        return {
            "categoria": category,
            "resposta_sugerida": response
        }
    except Exception:
        return {
            "categoria": "Indefinido",
            "resposta_sugerida": "Erro ao processar o email."
        }


@app.post("/upload-email")
async def upload_email(file: UploadFile = File(...)):
    content = read_email_file(file)

    if not content.strip():
        return {"error": "Arquivo vazio ou não suportado"}

    try:
        category = classify_email_with_ai(content)
        response = generate_response(category, content)

        return {
            "categoria": category,
            "resposta_sugerida": response
        }
    except Exception:
        return {
            "categoria": "Indefinido",
            "resposta_sugerida": "Erro ao processar o arquivo."
        }


@app.get("/ui", response_class=HTMLResponse)
def ui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/")
def root():
    return {"status": "API funcionando"}
