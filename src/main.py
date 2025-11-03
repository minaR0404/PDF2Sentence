from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import io
from src.pdf_loader import extract_texts_from_pdfs, extract_text_from_pdf_bytes

# text = extract_texts_from_pdfs(["tests/assets/n1310000.pdf"])
# print(text[:50])

app = FastAPI(
    title="PDF2Sentence API",
    description="Upload a PDF file and extract its text content using PyPDF.",
    version="1.0.0"
)

@app.post("/pdf2sentence")
async def extract_text(file: UploadFile = File(...)):
    """
    PDFファイルを受け取り、テキストを抽出して返すエンドポイント
    """
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="PDFファイルをアップロードしてください。")

    try:
        contents = await file.read()
        #text = extract_texts_from_pdfs(contents)
        text = extract_text_from_pdf_bytes(contents)

        if not text:
            return JSONResponse(
                status_code=204,
                content={"message": "PDFからテキストを抽出できませんでした。"}
            )

        return {"filename": file.filename, "text": text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"エラーが発生しました: {str(e)}")


@app.get("/")
def root():
    """
    動作確認用のルートエンドポイント
    """
    return {"message": "PDF Text Extraction API is running."}

# if __name__ == "__main__":
#     combined_text = extract_texts_from_pdfs(pdf_files)

#     # 出力ファイル
#     output_path = "output/combined_text.txt"
#     with open(output_path, "w", encoding="utf-8") as f:
#         f.write(combined_text)

#     print(f"✅ PDFのテキストを結合して保存しました: {output_path}")
