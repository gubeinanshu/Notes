```bash
# 升级系统到最新
sudo pacman -Syyu


# 配置源
kate /etc/pacman.conf


#1官方镜像源（包括 core， extra， community， multilib ）
sudo pacman-mirrors -i -c China -m rank //更新镜像排名
sudo pacman -Syy //更新数据源

#2archlinuxcn 源（中科大 ）
# USTC
[archlinuxcn]
 
SigLevel = Optional TrustedOnly
Server = https://mirrors.ustc.edu.cn/archlinuxcn/$arch

sudo pacman -Syyu //更新数据源
sudo pacman -S archlinuxcn-keyring //安装导入GPG key

#3aur源
#修改/etc/yaourtrc，去掉 # AURURL 的注释，修改为
AURURL=”https://aur.tuna.tsinghua.edu.cn”

#

#





```