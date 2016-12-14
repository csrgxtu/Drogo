### Drogo
命令行版的微信聊天。因为我只使用Linux作为我的开发环境，而公司，朋友间大多用微信作为即时通讯工具，所以这里借用开源的接口实现我自己定制的微信命令行聊天功能。支持的功能如下：
* 文本消息发送与接收（好友，群组）
* 图片发送与接收(好友，群组)
* 支持关注公众号的事件通知

### 如何使用
1, 安装Perl的包管理工具
```bash
sudo apt-get install cpanminus
```

2, 使用包管理工具安装微信协议解析包，IRC协议微信协议转换包
```bash
sudo cpanm Mojo::Weixin
sudo cpanm Mojo::IRC::Server::Chinese
```

3, 克隆当前repo
```bash
git clone https://github.com/csrgxtu/Drogo.git
```
4, 进入src代码目录, 拷贝IRCShell.pm到系统路径
```bash
cd Drogo/src
sudo cp IRCShell.pm /usr/local/share/perl/5.18.2/Mojo/Weixin/Plugin/IRCShell.pm
```
5, 启动服务端程序
```bash
perl weixinv1.pl
```
6, 启动irssi客户端
```bash
sudo apt-get install irssi

irssi -c 127.0.0.1 -p 6667
```

7, 进入IRC客户端后进行如下操作
```bash
/nick Archer #设置昵称为你的微信昵称
/list -YES # 列出当前的群组, 其中好友在群组 #我的好友中
/j #我的好友 # 进入一个群组
/msg JohnTian hey, man # 发送一个消息到好友
Alt^Left|Right # 使用组合键切换窗口到好友对话窗
sendFile /tmp/dog.png # 使用sendFile发送一个文件给好友
```
