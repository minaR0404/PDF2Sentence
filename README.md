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

\documentclass[a4paper,12pt]{article}
\usepackage{hyperref}
\usepackage{geometry}
\usepackage{listings}
\usepackage{xcolor}
\usepackage{titlesec}
\usepackage{enumitem}
\geometry{margin=25mm}

\lstset{
  basicstyle=\ttfamily\footnotesize,
  backgroundcolor=\color{gray!5},
  frame=single,
  breaklines=true,
  columns=fullflexible
}

\title{\Huge \textbf{PDF2Sentence ユーザーガイド}}
\author{Your Name}
\date{2025年}

\begin{document}

\maketitle
\tableofcontents
\newpage

\section{概要}

\textbf{PDF2Sentence} は、PDFファイルからテキストを抽出し、API経由で利用できる軽量な \textbf{FastAPI} アプリケーションです。  
PyPDF をベースに、OCRや図表対応などの拡張も可能な設計になっています。

\subsection*{主な機能}
\begin{itemize}
  \item PDFからのテキスト抽出（単一・複数対応）
  \item FastAPIベースのREST API
  \item Docker Composeによる簡単な実行
  \item pytest対応のテスト構成
\end{itemize}

\section{技術スタック}

\begin{center}
\begin{tabular}{|l|l|}
\hline
分類 & 使用技術 \\
\hline
言語 & Python 3.11 \\
フレームワーク & FastAPI \\
PDF処理 & PyPDF \\
インフラ & Docker / Docker Compose \\
テスト & pytest \\
CI/CD & GitHub Actions \\
\hline
\end{tabular}
\end{center}

\section{セットアップ手順}

\subsection{1. リポジトリのクローン}

\begin{lstlisting}[language=bash]
git clone https://github.com/<YOUR_USERNAME>/pdf2sentence.git
cd pdf2sentence
\end{lstlisting}

\subsection{2. ローカル開発（任意）}

\begin{lstlisting}[language=bash]
pip install -r requirements.txt
\end{lstlisting}

\subsection{3. Dockerイメージのビルド}

\begin{lstlisting}[language=bash]
docker compose build
\end{lstlisting}

\subsection{4. コンテナの起動}

\begin{lstlisting}[language=bash]
docker compose up
\end{lstlisting}

\noindent 成功すると、以下のようなメッセージが表示されます：
\begin{lstlisting}
Uvicorn running on http://0.0.0.0:8000
\end{lstlisting}

\subsection{5. APIへのアクセス}

\textbf{Swagger UI（自動ドキュメント）:}  
\url{http://localhost:8000/docs}

\noindent \textbf{cURL例:}
\begin{lstlisting}[language=bash]
curl -X POST "http://localhost:8000/upload-pdf/" \
  -F "file=@sample.pdf"
\end{lstlisting}

\noindent \textbf{レスポンス例:}
\begin{lstlisting}[language=json]
{
  "filename": "sample.pdf",
  "text": "ここにPDFの抽出テキストが入ります。"
}
\end{lstlisting}

\section{テストの実行}

\begin{lstlisting}[language=bash]
pytest -v
\end{lstlisting}

\section{Dockerコマンド一覧}

\begin{center}
\begin{tabular}{|l|l|}
\hline
操作 & コマンド \\
\hline
ビルド & docker compose build \\
起動 & docker compose up \\
停止 & docker compose down \\
再起動 & docker compose restart \\
\hline
\end{tabular}
\end{center}

\section{ディレクトリ構成（例）}

\begin{lstlisting}
pdf2sentence/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── pdf_loader.py
└── tests/
    └── test_pdf_loader.py
\end{lstlisting}

\section{環境変数（必要に応じて）}

\begin{center}
\begin{tabular}{|l|l|l|}
\hline
変数名 & 用途 & 例 \\
\hline
PYTHONUNBUFFERED & ログ出力を即時反映 & 1 \\
PORT & FastAPIポート番号 & 8000 \\
\hline
\end{tabular}
\end{center}

\section{参考: Dockerfile}

\begin{lstlisting}[language=Dockerfile]
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
\end{lstlisting}

\section{CI/CD 構成（GitHub Actions）}

\begin{itemize}
  \item main ブランチへの push 時に自動テストを実行
  \item Docker イメージをビルドして Docker Hub へ Push
\end{itemize}

\section{トラブルシューティング}

\begin{center}
\begin{tabular}{|l|l|}
\hline
症状 & 対処方法 \\
\hline
ModuleNotFoundError: No module named 'src' & docker-compose.yml の working\_dir を /app に設定 \\
Address already in use & ポート8000が使用中。別ポートに変更 \\
PDFが読めない & ファイル暗号化や破損の有無を確認 \\
\hline
\end{tabular}
\end{center}

\section{ライセンス}

MIT License \\
© 2025 Your Name or Organization

\section{著者情報}

\begin{itemize}
  \item \textbf{Your Name}
  \item Twitter: \href{https://twitter.com/yourhandle}{@yourhandle}
  \item GitHub: \href{https://github.com/yourusername}{github.com/yourusername}
\end{itemize}

\end{document}
