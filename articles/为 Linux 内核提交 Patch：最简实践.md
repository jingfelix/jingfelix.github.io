最近有一个向 Linux 内核提交 Patch (补丁) 的机会。历经卡在 SMTP 配置，被老板退回数次，被 Maintainer 建议修改后，终于被接纳进了 subtree……（Update：进入主线内核了！）

> ~~让自己的代码名留千古的机会~~ ❌
> 涉及的驱动可能被删除以避免侧信道攻击 ✅

## 什么是内核 Patch

众所周知，Linux 内核是世界上最大，最复杂，也是最重要的软件之一。其开发和维护依赖全球数以万计的开发者共同努力。

向 Linux 社区贡献代码的最基本方式是通过邮件的方式向内核维护者提交补丁（而非“现代化”地在代码托管平台发起 Pull Request）

> A patch is a small text document containing a delta of changes between two different versions of a source tree. FROM kernel.org.

补丁文件按照一定的格式介绍了代码变动的内容，以及进行这些修改的原因。经内核维护者审查通过后，这个补丁将集中合并进内核主线，或进入某个特殊的分支。

## 配置准备

本文基于 Ubuntu 介绍发送 Patch 的基本配置。

- git
- git send-email ( `apt install git-email`, `git-core` is also needed)
- diff
- perl

其中，git 用于版本控制与代码提交，git send-email 用于发送携带补丁的邮件，diff 用于比较文件差异，perl 作为 perl 解释器执行提交补丁所需的脚本。

为配置 smtp 发送邮件，需要在 git 配置文件`.gitconfig`中添加邮件相关的配置，以下为一个使用 Gmail 作为发送邮箱的例子：

```git
[user]
    name = YOURNAME
    # 此处的 email 应与发送邮件的邮箱一致
    email = YOURMAIL@gmail.com
[sendemail]
    from = YOURNAME <YOURMAIL@gmail.com>
    smtpencryption = ssl
    # 也可使用 tls 作为加密方式，端口应改为 578
    smtpserver = smtp.gmail.com
    smtpuser = YOURNAME
    smtpserverport = 465
    smtpAuth = LOGIN # 非必须
    chainreplyto = false # 非必须
    # tocmd 和 cccmd 是对获取内核邮件列表指令的简化，如果发送给自己以进行测试，只需注释即可
    tocmd = "`pwd`/scripts/get_maintainer.pl --nogit --norolestats --nol"
    cccmd = "`pwd`/scripts/get_maintainer.pl --nogit --norolestats --nom"
```

## 进行修改

想提交内核补丁，当然需要先获取一份内核代码！从 [kernel.org](kernel.org) 等处可以获取内核源码仓库，`git clone`一份到本地你喜欢的地方，并新建一个准备进行修改工作的分支。

```bash
git clone git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
git branch -b fix/blablabla
```

注意，为了避免出现冲突，需要保持本地代码与主线一致。开始修改前`git pull`是个好习惯。

## 描述改动

进行`commit`时，简单描述一下你所进行的改动，`commit`标题格式可以参考其他补丁，一般为`A: B: blablabla`的形式。使用`git commit -s`自动添加`Signed-off-by: YOUNAME <YOUREMAIL@gmail.com>`，否则你应在 patch 文件中添加该行信息。

```bash
git format-patch -1
```

`git format-patch`将在当前目录下生成一份包含标准邮件格式（但不一定是标准补丁格式）的`.patch`文件。这里的`-1`表示该补丁文件中仅应包含一个`commit`。

在`Subject: `与`Signed-off-by`行之间，需要对该补丁进行详细描述。我提交的补丁中描述了如何发现问题（Smatch 提供的错误信息），错误原因（`ioremap` 分配的内存没有取消映射）和修改方式（改为`devm_ioremap`以保证在设备移除时取消内存映射）

别忘了测试！你可以选择全量编译整个内核，或在你修改的模块里仅编译你修改的部分（比如一个驱动）

## 发送，以及等待

格式检查：使用内核源码中内置的脚本：

```bash
$PATH_TO_KERNEL/scripts/checkpatch.pl YOUR_PATCH.patch
```

一个常见的错误是：

```bash
WARNING: Possible unwrapped commit description (prefer a maximum 75 chars per line)
```

这是因为在 Linux 内核的`COMMIT_MSG`和 Patch 需要能够在限长 80 字符的终端机正常显示，因此每行不能超过 80 字（believe it or not，内核中充满神奇的古老规定）按报错信息修改即可。

还记得我们在`.gitconfig`中添加的`tocmd`和`cccmd`吗？

```git
tocmd = "`pwd`/scripts/get_maintainer.pl --nogit --norolestats --nol"
cccmd = "`pwd`/scripts/get_maintainer.pl --nogit --norolestats --nom"
```

`tocmd`行将自动获取收件人，即修改部分的内核维护者的邮件。同理，`cccmd`行获取抄送人邮件列表。这样可以简化使用命令行发送邮件时的“CLI心智负担”。

```bash
git send-email YOUR_PATCH.patch
```

没错，最终的发送指令就这么简单！

如果想先发给自己，或者其他有经验的人为你 Review 一下，避免不合理的 Patch 引起内核维护者的怒火呢？你可以将`tocmd`和`cccmd`注释掉，并在发送时添加`--to`和`--cc`选项，指定发送/抄送人即可。

```bash
git send-email --to RECEIVE@gmail.com --cc YOURNAME@gmail.com YOUR_PATCH.patch
```

正是发送后，你需要的就只有……耐心地等待。Well，内核维护者们非常勤奋，但没有人能保证及时审查和回复所有邮件，对吧？

假如几个星期后你的补丁邮件依然无人问津（这并不罕见），你可以发送 PING 或 RESEND 来提醒维护者。

```bash
git fromat-patch -1 --subject-prefix='PING'
# or
git format-patch -1 --subject-prefix='RESEND'
```

## 修改，v2，v3，v4……

经过漫长的等待，一封`Re: PATCH`叩响了你邮箱的大门——迎接你的也许是一句简单的“Applied, thanks”，也许是满满的牢骚和怒火（当然，大多数时候是礼貌而友好的）

请注意，新的 PATCH，即`PATCH v2`，应该和最初一样，在原汁原味的HEAD分支上进行改动，而不是在你的 Commit 的基础上提交新的代码。

按意见修改后，你就可以发出`PATCH v2`了。记得在`Reviewed by`之后添加 Changelog 信息，即你进行了哪些修改。比如：

```bash
v2 -> v3: Directly deleted 'base' and its related code based on master.
v1 -> v2: Directly deleted 'base' and its related code based on PATCH v1.
```

新邮件的主题也需要进行修改：

```bash
git format-patch -1 --subject-prefix='PATCH v2'
```

发送新补丁的过程和第一次一样，注意要发送的文件别选错了。

也许修改补丁的过程要重复很多次，也许你还需要发送 v3，v4，但请不要气馁！

## 接收之后

在你的补丁被维护者接纳之后，它会首先被合并进该模块的子树（可以在[git.kernel.org](git.kernel.org)找到），然后和其他补丁一起集中提交给 Linus，最后进入主线内核。大功告成！

## 其他需要注意的

- 只回复邮件，不发送补丁，也可以使用`git send-email`，具体需要的指令可以在[https://lore.kernel.org/lkml/](https://lore.kernel.org/lkml/)你要回复的邮件后找到。
- 本文没有涉及一次发送多个 PATCH 的情况。你可以在[这里](https://docs.kernel.org/translations/zh_CN/process/submitting-patches.html)找到更多资料。
