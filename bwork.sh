sshpass -p "41424344" ssh  192.168.43.1 -p 8022 tcpsvd -vE 0.0.0.0 1024 ftpd -w /sdcard/ &
echo started ftp
sleep 5
rm -rf bitbns.csv*
wget ftp://192.168.43.1:1024/Pictures/bitbns.csv 
echo downloaded file
python3 insertbit.py
python3 backtest_tri_bitbns.py
