[TOC]

# Git基本操作 #

## **==Git命令==** ##

> * `git log`：显示更改信息，`:q`退出`vim`，简单版`git log --oneline`；
>
>   `git log -p -2`显示最新两条的详细变化内容。
>
>
> * `git status -s`：简洁版的状态显示；
> * `git diff`：只显示没有$add$ 前的状态；
> * `git add .`：$add$ 所有文件；
> * `git diff —cached`：$add$ 之后想查看与未修改的不同；
> * `git commit -am "内容"`：可以跳过 $add$ 直接 $commit$ 。

### ==忽略某些文件== ###

这样不会太混乱。

> ``` git
> touch .gitignore
> vim .gitignore
> ```

#### ==移除文件== ####

> ```python
> # 只移除远程仓库的文件，保留本地文件
> git rm --cached test.py  # git rm --cached -r 文件夹名
> git commit -m "内容"
> git push  # git push -u origin master
> ```

##### ==移动文件(修改名字)== #####

> ```python
> git mv 原名 修改名
> ```

##### ==撤销上一次修改== #####

> ```python
> # 想撤销修改某一文件时，好像只返回了上一次修改
> git checkout -- name
> ```

##### ==reset所有状态都返回== #####

> 假如修改某文件（a.py）之后将其 $add$ 进暂缓之后，想要返回非暂缓区：
>
> ```python
> git reset a.py
> ```
>
> 回到没有修改的状态：
>
> ```python
> git reset --hard HEAD
> ```
>
> add并且commit之后想回到某个版本：
>
> ```python
> git log  # git reflog (可以查看未来变化版本)
> # git reset --hard HEAD
> git reset --hard HEAD^1  # 回到上一个版本就是1个^，回到上几个就是几个^
> git reset --hard HEAD~1  # 回到上一个版本就是1，回到上n个就是n
> git reset --hard afee5c4  # 回到特定版本
> git reset --hard HEAD@{1}  # 回到特定版本
> ```
>

##### ==checkout对单个文件返回== #####

> ```python
> git checkout 418c806 -- git.py  # 哈希值 -- 文件名字
> ```
>
> 这样能对单个文件回到某个版本。\* 即使当前版本没了这文件，只要能回到有这文件的版本就能找回！
>
> 想要修改的话，继续执行
>
> ```python
> git add git.py
> git commit -m "内容"
> ```

##### ==上传步骤== #####

+ 先`cd`到需要上传的文件夹中，如果没有`.git`文件的话需要`git init`；
+ 将需要上传的文件先`add`，`git add ***`；
+ 再添加说明，`git commit -m "文件说明"`；
+ 连接需要上传到的`repository`，`git remote add origin git@github.com:HELIN007/python3.git`，后面的是`repository`的名字；
+ 最后在上传，`git push -u origin master`。

## 分支 ##

```python
git log --oneline --graph  # 图形显示log
git branch  # 查看分支
git branch ***  # 创建分支***
git checkout ***  # 切换分支
# 新建并切换到分支***
# git checkout -b ***
git branch -d ***  # 删除分支(得切换到另外分支才能删除此分支)
git merge --no-ff -m "保留merge信息" ***  # 不快速合并，并保留信息
git branch -v  # 查看各个分支最后一个提交对象的信息
git branch --merged  # 查看哪些分支已被并入当前分支，不带*的其实可以删掉，因为已经合并完了
git branch --no-merged  # 显示还未合并进来的分支
git branch -D ***  # 强制删除***分支
git branch -av  # 显示本地及远程分支、没有v的话不会出注释
git push origin :***  # 删除远程分支，***为远程分支名，冒号前有空格
git status  # 暂时存储工作，不需要commit之后才能切换分支
git stash list  # 查看现有的储藏
git stash apply stash@{1}  # 可以应用更早的存储，如果不指明，Git 默认使用最近的储藏并尝试应用它
git stash drop  # apply 选项只尝试应用储藏的工作——储藏的内容仍然在栈上。要移除它，可以运行 git stash drop，加上希望移除的储藏的名字
git stash pop  # 重新应用储藏，同时立刻将其从堆栈中移走
```

\* 当主分支和次分支同时都修改过的情况时，两者合并就会出现冲突。此时需要人工手动解决冲突（直接操作文件，git在文件里有提示），然后再

```python
git merge 次分支
git commit -am "内容"
```

## 打标签Tag ##

**\*** 给想要的版本打上标签的话就是独立的一部分，以后更改其他分支什么的都不受影响。想要更新版本，就继续打标签。

```python
git log --oneline --graph  # 查看想打标签的哈希值
git tag -a v1.0 哈希值 -m "内容"  # 给这个版本打上标签，并写点内容
git push origin v1.0  # 将这个版本传到远程库

git show v2.0  # 查看标签的内容
git tag  # 查看已有标签
git tag -l 'v1.*'  # 只显示出1.几版本

git push origin --tags  # 一次推送所有本地新增的标签上去

# # 打错了标签的话
# 未上传到远程库中
git tag -d v1.0
# 上传到远程库的话
git tag -d v1.0
git push origin :refs/tags/v1.0  # 固定句式，就改后面的版本号
```
