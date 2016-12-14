#!/usr/bin/env perl
use Mojo::Weixin;
my $client = Mojo::Weixin->new();
$client->load("IRCShell",data=>{
    listen=>[ {host=>"127.0.0.1",port=>6667},], #可选，IRC服务器监听的地址+端口，默认0.0.0.0:6667
    load_friend => 1, #默认是0 是否初始为每个好友生成irc虚拟帐号并加入频道 #我的好友
});
$client->load("ShowMsg");
$client->run();
