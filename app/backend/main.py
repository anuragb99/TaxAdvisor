from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
import tempfile
from .db import ensure_userfinancials_table
from .pdf_extract import extract_userfinancials_from_pdf

app = FastAPI()

# CORS for local frontend testing (if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    ensure_userfinancials_table()

@app.get("/api/health")
def health_check():
    return {"status": "ok"}

@app.post("/api/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename or not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp:
            contents = await file.read()
            tmp.write(contents)
            tmp_path = tmp.name
        # File is now closed, safe to open with PyPDF2
        data = extract_userfinancials_from_pdf(tmp_path)
        os.remove(tmp_path)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Extraction failed: {str(e)}")

# Serve static files (frontend)
frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend")
app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend") 