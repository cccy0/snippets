#ubuntu18.04

1. 虚拟网络编辑器-更改设置-nat

子网ip 192.168.xx.0 不变 子网掩码不变

nat设置 网关 192.168.xx.2

我的是162.168.98.2、

2. 物理机网络适配器

适配器选项

vmnet8

tcp4 属性

192.168.xx.1

默认网关 192.168.xx.2


3. 

vim /etc/netplan/01xxxxx.yaml



```yaml

# Let NetworkManager manage all devices on this system
network:
  version: 2
  renderer: NetworkManager
  ethernets:
    ens33:                      #网卡名，以ubuntu操作系统的网卡名称为准
      dhcp4: no                 #ipv4关闭dhcp，用static模式
      dhcp6: no                 #ip6关闭dhcp
      addresses:
        - 192.168.98.163/24     #本机IP地址
      gateway4: 192.168.98.2    #vmware网关的的IP地址
      nameservers: # 没这个虚拟机上不了网
        addresses: [192.168.98.2]
```


sudo netplan apply

