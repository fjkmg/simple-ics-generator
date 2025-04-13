import json
from ics import Calendar, Event
from datetime import datetime, timedelta
import pytz

# 日本時間
japan = pytz.timezone("Asia/Tokyo")

# ==== 入力JSONファイル読み込み ====
with open("events.json", "r", encoding="utf-8") as f:
    events_data = json.load(f)

# ==== ICSカレンダーの作成 ====
calendar = Calendar()

# ==== 各イベントを処理 ====
for item in events_data:
    title = item["title"]
    start_time_str = item["start_time"]
    duration = timedelta(minutes=item["duration_minutes"])
    dates = item["dates"]
    location = item.get("location", "")  # 任意項目
    description = item.get("description", "")  # 任意項目

    for date_str in dates:
        # 開始時刻を作成
        full_datetime_str = f"{date_str} {start_time_str}"
        dt = datetime.strptime(full_datetime_str, "%Y-%m-%d %H:%M")
        dt_japan = japan.localize(dt)

        # イベント作成
        event = Event()
        event.name = title
        event.begin = dt_japan
        event.duration = duration
        event.location = location
        event.description = description

        calendar.events.add(event)

# ==== 出力 ====
with open("multi_schedule.ics", "w", encoding="utf-8") as f:
    f.writelines(calendar.serialize_iter())

print("ICSファイル 'multi_schedule.ics' を作成しました。")
