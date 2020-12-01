from datetime import datetime as dt, timedelta
last_seen=dt.now()-timedelta(days=2)
print(last_seen , dt.now())
print((dt.now() - last_seen).days < 180)
print((last_seen + timedelta(days=180)) > dt.now())
print(((dt.now() - last_seen)) < timedelta(days=180))