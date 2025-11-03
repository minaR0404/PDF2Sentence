# 📄 概要

このリポジトリは、**pypdf**（旧 **PyPDF2**）を使用して **PDF からテキストを抽出**するシンプルなツールです。  

- 🏃‍♂️ **テキスト化された PDF の高速抽出**に最適  
- 🧠 **スキャン（画像）PDF** にも対応（`pytesseract` + `pdf2image` による OCR モード）  
- ⚙️ **CLI / Python ライブラリ** 両対応 — スクリプト・バッチ処理・Web API への組み込みが容易  

---

# 🔧 主な機能

- 📘 **単一 PDF** または **ディレクトリ内の複数 PDF** をまとめて処理  
- 🧩 **ページ単位 / 全文抽出** の選択が可能  
- 🗂️ 出力形式：**標準出力（STDOUT）**, **テキストファイル**, **JSON**  
- 🔍 **スキャンPDF向け OCR オプション**（必要に応じて有効化）  

---

> 💡 **Tips:**  
> OCRを利用する場合は、`tesseract` と `poppler` のインストールが必要です。  
> （例：macOS → `brew install tesseract poppler`）

*name changed.  
*brach update.

# 📘 PDF2Sentence

PDF2Sentenceは、PDFファイルからテキストを抽出し、REST APIとして提供する軽量な **FastAPIアプリケーション** です。  
Docker Composeを利用して簡単に起動できます。

---

## 🚀 機能概要

- 🧩 **PDFテキスト抽出**（単一・複数ファイル対応）  
- ⚡ **FastAPIベースのREST APIサーバ**  
- 🐳 **Docker Compose対応**  
- 🧪 **pytestでの自動テスト**  
- 🔧 **拡張可能なモジュール構成**

---

## 🧱 技術スタック

| 分類 | 使用技術 |
|------|-----------|
| 言語 | Python 3.11 |
| フレームワーク | FastAPI |
| PDF処理 | PyPDF |
| インフラ | Docker / Docker Compose |
| テスト | pytest |
| CI/CD | GitHub Actions（任意） |

---

## ⚙️ セットアップ手順

### 1️⃣ リポジトリのクローン

```bash
git clone https://github.com/<YOUR_USERNAME>/pdf2sentence.git
cd pdf2sentence
```

### 2️⃣ 依存パッケージのインストール（ローカル開発用）
```bash
pip install -r requirements.txt
```

### 3️⃣ Dockerイメージのビルド
```bash
docker compose build
```

### 4️⃣ コンテナの起動
```bash
docker compose up
```

実行後、以下のようなメッセージが出れば成功です：
Uvicorn running on http://0.0.0.0:8000