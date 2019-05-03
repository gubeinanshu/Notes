内存卡根目录新建文件: wpa_supplicant.conf
```
country=CN
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
 
network={
	ssid="301301"
	psk="18367116191"
	key_mgmt=WPA-PSK
	priority=1
}
 
network={
	ssid="TP-LINK_954D"
	psk="vvcn1101"
	key_mgmt=WPA-PSK
	priority=2
}
```