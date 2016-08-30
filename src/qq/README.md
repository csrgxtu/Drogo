#### 命令行版本的QQ
这是为了解决我在Linux下与公司内部其它人员协作的问题。

```bash
启动, 扫描二维码登陆
python main.py [qqnumber]
Example: python main.py 122121212

查看联系人, 参数任选一个,例如buddy
contact buddy|group|discuss
Example: contact buddy

设置昵称映射
alias qqId nickname
Example: alias 3766945211 archer

查看昵称映射
listalias

发送消息, 通过qqId和昵称发送
sendmsg qqId content
Example: sendmsg 3766945211 yo man!

sendaliasmsg nickname content
Example: sendaliasmsg archer yo man!

退出
q
```
