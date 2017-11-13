## In Ubuntu/Debian : ##
```
cd ~/.config/google-chrome/Default

sqlite3 History "select datetime(last_visit_time/1000000-11644473600,'unixepoch'),url from  urls order by last_visit_time desc" > ~/hist.txt

python3 analyze.py
```
