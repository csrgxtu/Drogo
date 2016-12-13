#!/usr/bin/env perl
use Mojo::Weixin;

my $client = Mojo::Weixin->new();
$client->load("IRCShell",data=>{
    listen=>[ {host=>"127.0.0.1",port=>6667},], #可选，IRC服务器监听的地址+端口，默认0.0.0.0:6667
    load_friend => 1, #默认是0 是否初始为每个好友生成irc虚拟帐号并加入频道 #我的好友
});
# $client->load("ShowMsg");

#ready事件触发时 表示客户端一切准备就绪：已经成功登录、已经加载完个人/好友/群信息等
#你的代码建议尽量写在 ready 事件中
$client->on(ready=>sub{
    my $client = shift;

    #设置接收消息事件的回调函数，在回调函数中对消息以相同内容进行回复
    $client->on(receive_message=>sub{
        my ($client,$msg)=@_;
        # $msg->reply($msg->content); #已以相同内容回复接收到的消息
        #你也可以使用$msg->dump() 来打印消息结构
        # print $msg->dump()
        if($msg->type eq "friend_message"){#接收到好友消息
            my $friend = $msg->sender; #获取到该好友对象
            my $rcvMsg = $friend->displayname . ":" . $msg->content;
            system("printf '\7'");
            system("notify-send " . $rcvMsg);
            print $rcvMsg;
            # print "我的好友：" . $friend->displayname . "给我发了一个消息，消息的内容是：" . $msg->content;
        }
        elsif($msg->type eq "group_message"){#接收到群消息
            my $group = $msg->group;    #获取到消息对应的群组对象
            my $sender = $msg->sender;  #获取到发送该消息的群成员对象

            print $sender->displayname . "在群：", $group->displayname . "中发了一条消息，消息的内容是：" . $msg->content;
        }
        elsif($msg->type eq "group_notice"){
            my $group = $msg->group;    #获取到消息对应的群组对象
            print "在群：", $group->displayname . "中收到了一条群提示消息，消息的内容是：" . $msg->content;
        }
    });

    #你的其他代码写在此处

});

$client->run();
