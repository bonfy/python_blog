title: MAC下的定时任务
date: 2014-10-25 16:43:49
---

linux之下可以用 crontab 不过在MAC下无效

现在说说MAC下吧  用launchctl 

cd $HOME/Library/LaunchAgents 其实就是/Users/bonfy/Library/LaunchAgents

然后 touch com.bonfy.crontabSpider.plist
然后 打开编辑：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.bonfy.crontabSpider</string>

  <key>ProgramArguments</key>
  <array>
    <string>/Users/bonfy/Desktop/task.sh</string>
  </array>

  <key>Nice</key>
  <integer>1</integer>

  <key>StartInterval</key>
  <integer>60</integer>

  <key>RunAtLoad</key>
  <true/>

  <key>StandardErrorPath</key>
  <string>/tmp/AlTest1.err</string>

  <key>StandardOutPath</key>
  <string>/tmp/AlTest1.out</string>
</dict>
</plist>
```

保存

再 launchctl load com.bonfy.crontabSpider.plist
就开始执行了
重新启动 也会自己启动的
