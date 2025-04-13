# 📅 ics-scheduler

複数の予定を指定した日付に従って `.ics` カレンダー形式で出力する Pythonツール  
Googleカレンダーなどに簡単にインポートできる

## 特徴

- 各予定の **日時・タイトル・場所・説明・所要時間** を指定可能
- 予定ごとに実施する **日付リストを明示的に指定**
- **日本時間（Asia/Tokyo）に対応**
- `ics` 形式で出力
- JSONファイルから予定を読み込み可能

---

## 必要なライブラリ

Python 3.7 以上  
以下のパッケージを使用する：

```bash
pip install -r requirements.txt
```

```txt
# requirements.txt
ics
pytz
```

---

## 入力ファイル

```json
[
  {
    "title": "ゼミ",
    "start_time": "18:00",
    "duration_minutes": 90,
    "location": "3号館401教室",
    "description": "毎週の研究ゼミ。資料を持参。",
    "dates": ["2025-04-15", "2025-04-22", "2025-05-13"]
  },
  {
    "title": "英語の授業",
    "start_time": "10:30",
    "duration_minutes": 60,
    "location": "オンライン",
    "description": "Zoomリンクはポータルに掲載。",
    "dates": ["2025-04-16", "2025-04-23"]
  }
]
```

---

## 使い方

### 1. JSONファイルを用意（例：`events.json`）

### 2. Pythonスクリプトを実行

```bash
python generate_ics.py
```

### 3. 出力ファイル：`multi_schedule.ics`

---

## ファイル構成（例）

```
ics-scheduler/
├── generate_ics.py
├── events.json
├── multi_schedule.ics
├── requirements.txt
└── README.md
```
