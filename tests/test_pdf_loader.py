from fastapi.testclient import TestClient
from src.main import app
from src.pdf_loader import extract_text_from_pdf

# def test_extract_text_from_pdf():
#     text = extract_text_from_pdf("tests/assets/ss_251024.pdf")
#     assert isinstance(text, str)
#     assert len(text) > 0
#     print(text[:100])

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "PDF Text Extraction API" in response.json()["message"] or "running" in response.json()["message"]

def test_extract_text_invalid_file():
    response = client.post("/pdf2sentence", files={"file": ("test.txt", b"not a pdf")})
    assert response.status_code == 400
