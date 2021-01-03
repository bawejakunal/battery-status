This is a simple python script to report laptop battery status to an MQTT topic.

Install as a cron on Linux

`*/5 * * * * <path to battery-status directory>/battery-status/battery-state.py -b <broker_address> &> /dev/null`

Install as a cron on Windows

`SCHTASKS /Create /SC MINUTE /MO 5 /TN batterystatus /TR  "C:\Users\<UserName>\AppData\Local\Microsoft\WindowsApps\python.exe" "<path to battery-status directory>\battery-status\battery-state-win.py" "-b" "<broker_address>"`