sshpass -p "41424344" ssh  192.168.43.1 -p 8022 tcpsvd -vE 0.0.0.0 1024 ftpd -w /sdcard/ &
echo started ftp
sleep 5
rm -rf wazirx.csv*
wget ftp://192.168.43.1:1024/Pictures/wazirx.csv 
echo downloaded file
python3 insert.py
python3 backtest_tri_wazirx.py
