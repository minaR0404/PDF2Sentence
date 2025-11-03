import os
from pypdf import PdfReader
from tqdm import tqdm
import argparse
from io import BytesIO

def extract_text_from_pdf_bytes(file_bytes: bytes) -> str:
    """
    バイトデータ（メモリ上のPDF）からテキストを抽出する。
    """
    text = ""
    try:
        pdf_stream = BytesIO(file_bytes)
        reader = PdfReader(pdf_stream)
        for page in reader.pages:
            text += page.extract_text() or ""
    except Exception as e:
        print(f"[Error] PDFの抽出中にエラー: {e}")
    return text


def extract_text_from_pdf(file_path: str) -> str:
    """
    単一のPDFファイルからテキストを抽出する。
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"PDFファイルが見つかりません: {file_path}")

    text = ""
    try:
        with open(file_path, "rb") as f:
            reader = PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() or ""
    except Exception as e:
        print(f"[Error] {file_path} の抽出中にエラー: {e}")
    return text


def extract_texts_from_pdfs(pdf_paths: list[str]) -> str:
    """
    複数のPDFを読み込み、1つの文章データとして結合する。
    """
    all_text = ""
    for path in tqdm(pdf_paths, desc="Extracting PDFs"):
        all_text += extract_text_from_pdf(path) + "\n\n"
    return all_text


# ========================================
# CLI化した __main__ ブロック
# ========================================
def main():
    parser = argparse.ArgumentParser(
        description="PDFからテキストを抽出するシンプルツール"
    )
    parser.add_argument(
        "pdfs", nargs="+", help="抽出対象のPDFファイルパス（複数指定可）"
    )
    parser.add_argument(
        "-o", "--output", help="抽出結果を保存するファイル名（省略時は標準出力）"
    )
    parser.add_argument(
        "--head", type=int, default=100, help="出力を先頭何文字だけ表示するか（デフォルトは100文字）"
    )

    args = parser.parse_args()

    # PDFファイル存在チェック
    missing = [p for p in args.pdfs if not os.path.exists(p)]
    if missing:
        print(f"[Error] 以下のファイルが見つかりません:\n" + "\n".join(missing))
        return

    # 抽出
    combined_text = extract_texts_from_pdfs(args.pdfs)

    # 先頭表示指定
    display_text = combined_text
    if args.head > 0:
        display_text = combined_text[: args.head]

    # 出力
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(combined_text)
        print(f"抽出結果を {args.output} に保存しました。")
    else:
        print("\n===== 抽出結果 =====")
        print(display_text)
        print("====================")
        print(f"抽出完了 ({len(args.pdfs)} ファイル処理)")

if __name__ == "__main__":
    main()