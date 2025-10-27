from pdf_loader import extract_texts_from_pdfs

# 読み込み対象のPDFファイル（相対パス or 絶対パス）
pdf_files = [
    "data/sample1.pdf",
    "data/sample2.pdf",
]

if __name__ == "__main__":
    combined_text = extract_texts_from_pdfs(pdf_files)

    # 出力ファイル
    output_path = "output/combined_text.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(combined_text)

    print(f"✅ PDFのテキストを結合して保存しました: {output_path}")
