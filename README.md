This is a simple python script to report laptop battery status to an MQTT topic.

Install as a cron

`*/5 * * * * /home/kunal/workspace/battery-status/battery-state.py -b <broker_address> &> /dev/null`

`SCHTASKS /Create /SC MINUTE /MO 5 /TN batterystatus /TR  "C:\Users\Kunal Baweja\AppData\Local\Microsoft\WindowsApps\python.exe C:\Users\Kunal Baweja\workspace\battery-status\battery-state-win.py"`