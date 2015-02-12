title: blog同步
date: 2014-01-05 14:40:35
tags: blog
---
blog建立的初衷是 你经常有很多东西去google或者baidu，当然一般你查到了你想要的东西你一般都会直接将这个网页设置为书签，但是这个还是会有两个问题：
1. 书签多了之后，如何管理？我就发现很多我以前找到过的有用的文章或者知识点，后来想起就很难再找到了
2. 书签往往保存的是一个网站路径，这个网页可能谈的事情多种多样，并不是都是你感兴趣的，你想要的。你查的可能是里面的一个命令，或者一个问题的解决方案，我每次不用将这篇文章从头看到底

说到底还是我的记忆总是那种片段性记忆，只记得某个时间点干过些啥，但是具体怎么操作的可能并不是会记得很清楚，所以这个Blog的初衷可能为了方便记忆，和存放一些自己感兴趣的东西

let's go ahead：
如果我的电脑就一个，那么我建blog之类的只在一个文件夹内修改，那么我也就没其他问题了，可是我可能家里一个工作电脑，单位一个，那么万一我要记录的时候就有问题了，我必须保证两边是同步的，当然一个好方法 就是github保存。

当然我现在用的是 hexo,它可以自动deploy到 github.io，但是这里面都是编译的文件，而且我还没找到方法增量添加

所以我这里的解决方案是我还得再见一个repo，存放原始文件，这样我每次修改，保存到github，修改的时候可以先clone，然后再上传。这只能是目前我能想到的解决办法了。

Let's go ahead：

先访问github.com 创建一个repo： xxx
接下去：

```git
touch README.md(windows下没有touch)
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/username/xxx.git
git push -u origin master

```

先在一台PC上建立xxx，完成代码
```git
git add.
git commit -m "xxxxxx"
git push
```

另一台PC上直接
```git
git clone https://github.com/useranem/xxx.git 
```