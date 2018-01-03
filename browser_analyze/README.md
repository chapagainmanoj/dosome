## In Ubuntu/Debian : ##
export browsing history: chrome
```
cd ~/.config/google-chrome/Default
sqlite3 History "select datetime(last_visit_time/1000000-11644473600,'unixepoch'),url from  urls order by last_visit_time desc" > ~/hist.txt
```
export browsing history: mozilla
```
cd .mozilla/firefox/*.default
sqlite3 places.sqlite "select datetime(last_visit_date/1000000-11644473600,'unixepoch'),url from  moz_places order by last_visit_date desc" > ~/moz_hist.txt
```
```
python3 analyze.py
```

## Requirements ##
python3-tk
sqlite3
