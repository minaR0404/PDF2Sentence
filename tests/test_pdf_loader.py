from src.pdf_loader import extract_text_from_pdf

def test_extract_text_from_pdf():
    text = extract_text_from_pdf("tests/assets/ss_251024.pdf")
    assert isinstance(text, str)
    assert len(text) > 0
    print(text[:100])
