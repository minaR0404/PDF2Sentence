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
| クラウド | AWS EC2 |

---

## ⚙️ セットアップ手順

### 1️⃣ リポジトリのクローン

```bash
git clone https://github.com/minaR0404/pdf2sentence.git
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
```bash
Uvicorn running on http://0.0.0.0:8000
```

---

## 🌐 APIの利用方法

### 📘 Swagger UI（APIドキュメント）

ブラウザで以下にアクセス：

👉 [http://localhost:8000/docs](http://localhost:8000/docs)

### 💻 curlでのAPI呼び出し例

```bash
curl -X POST "http://localhost:8000/pdf2sentence/" \
  -F "file=@tests/assets/n1310000.pdf"
```

### 📦 レスポンス例
```json
{
  "filename": "n1310000.pdf",
  "text": "技術の発展は、人間の能力を拡張し、できることを強化してきた。人間等の知的活動をコン\nピュータにより再現する人工知能（Artificial Intelligence：AI）は、70年以上の開発の歴史のな\nかで進化を続け、企業活動、国民生活に浸透しつつある。特に2022年頃から急速に普及した生成\nAIは、その進化の飛躍的な例と言える。生成AIは、人間のように文章や画像を生成し、多岐にわ\nたるタスクを自律的にこなすことができる革新的な技術である。これにより、広告やマーケティン\nグ、コンテンツ制作をはじめ様々なビジネスにおいて大きな変革がもたらされている。我々の生活\nにおいても、自然言語による対話インターフェースがますます普及し、スマートスピーカーや\nチャットボットが私たちの日常に溶け込み、生活を大きく変えている。また、AIはXR（拡張現\n実） 、ロボティクス等の他の技術・サービスと組み合わされることで、より一層の発展が期待され\nている。例えば、生成AIを用いたXR技術により、臨場感のある仮想空間を提供することで、教\n育やエンターテイメントの分野で新たな価値体験を生み出している。また、AIを搭載したロボッ\nトが、 製造業から介護など様々な分野で活躍し、 作業の自動化や人々の生活の支援に貢献している。\nこうしたAI、XR等情報通信技術（ICT）..."
}
```

### 🧪 テスト実行
```bash
pytest -v
```

---

## 🧑‍💻 著者情報

| 項目 | 内容 |
|------|------|
| **Author** | minaR0404 |
| **GitHub** | [https://github.com/minaR0404](https://github.com/minaR0404) |

## 📜 ライセンス

**MIT License**  
© 2025 minaR0404
