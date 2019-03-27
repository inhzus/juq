# Juq
Yuque SDK and command line tool.

## CMD Tool

### Installation

```
pip3 install juq
```

使用前需要配置 [Personal Access Token](https://www.yuque.com/settings/tokens), 取得 TOKEN 后

```
juq config set TOKEN "your token here"
```

即可正常使用.

### Quickstart

```bash
$ juq config set TOKEN "YourPersonalAccessToken"
# 设置 TOKEN

$ juq user info
# 查看个人信息
   id: 294604
login: inhzus
 name: inhzus
 desc: None

$ juq user repos inhzus  # juq user repos {id}
# 查看用户 inhzus 的所有知识库
id: 242345      slug: book      name: inhzus
id: 242344      slug: kb        name: Default repository

$ juq repo info inhzus/book  # juq repo info {repo_id}
# 查看用户 inhzus 的 book 知识库的信息
     id: 242345
   slug: book
   name: inhzus
  items: 7
 public: 0
user_id: 294604
updated: 2019-03-27T03:11:07.000Z

$ juq repo create -h
# 查看创建知识库的帮助信息
# 省略

$ juq repo create test "test repo" -p 2 -d "描述"
# 创建路径名"test", 名称"test repo", 公开程度 2, 描述为"描述"的知识库.
id: 251878      slug: test      name: test repo

$ juq repo toc inhzus/book
# 查看目录结构, 可以直接看出文档间的目录结构.
id: 1396889     slug: 2019-01-31-welcome        title: 2019-01-31-welcome.md
id: 1396890     slug: 2019-02-06-kmp-review     title: 2019-02-06-kmp-review.md
id: 1396908     slug: test      title: Untitled
id: 1432501     slug: 6ba67bd   title: 2019-03-26-juq-technical-docs.md

$ juq doc toc inhzus/book 1432501 -a 1396889 -d 1
# 修改目录结构, 将第四个文档移至第一个文档后, 且深度为 1
id: 1396889     slug: 2019-01-31-welcome        title: 2019-01-31-welcome.md
|-id: 1432501   slug: 6ba67bd   title: 2019-03-26-juq-technical-docs.md
id: 1396890     slug: 2019-02-06-kmp-review     title: 2019-02-06-kmp-review.md
id: 1396908     slug: test      title: Untitled

$ juq doc create inhzus/test doc.md -s testdoc -t "测试文档" -p
# 在 inhzus/test 知识库创建文档, 使用本地的 doc.md 文件, 路径名"testdoc", 标题"测试文档", 公开

$ juq doc delete inhzus/test 1436607
# 删除文档

$ juq repo delete inhzus/test
# 删除知识库
```

### Usage

juq 的使用均在命令行下执行.

以下说明中, "[]"为可选参数, "|"为选择参数, "{}"为参数名

参数(如文档标题)中若带有特殊符号, 推荐使用引号.

#### Help

查看指令的帮助文档, 使用 -h 参数即可:

```
juq -h
juq config -h
juq config set -h
```

#### <span id="config">Config</span>

```bash
juq config get {key}
# 查看配置
juq config set {key} {value}
# 设置配置信息
juq config reset
# 重设所有配置信息, 请确认再三执行.
```

配置信息可以通过以上指令实现, 也可以直接编辑 `~/.juq` 文件, 如:

```yaml
TOKEN: your_token_here
TIMEOUT: 5
```

#### User

用户的唯一标识为 {login} 或 {id}

{login} 即用户路径名, {id} 为语雀数据库中的标识号.

```bash
juq user info [{login}|{id}]
# 指定用户的信息. 若无参数, 即 TOKEN 用户的信息, 以下同
juq user docs [-q {q}] [-o {offset}]
# TOKEN 用户的文档. q 为模糊搜索关键词; offset 为页偏移(每页 20), 以下同
juq user groups [{login}|{id}]
# 指定用户参与的团队
juq user repos [{id}|{login}] [-t Book|Design|all] [-o {offset}]
# 指定用户的知识库. type, 类型: 默认为 all, 全部.
juq user recent [-t Book|Doc] [-o {offset}]
```

#### Group

团队的唯一标识与用户规律相同.

```bash
juq group info {login}|{id}
# 指定团队的信息
juq group repos {login}|{id} [-t Book|Design|all] [-o {offset}]
# 指定团队的知识库
```

#### Repo

知识库的唯一标识为 ({login}|{id})/{slug} 或 {id}, 以下都使用 {repo_id} 代指.

其中, {login} 和 {id} 是用户或团队的标识, {slug} 为知识库的知识库的路径名, {id} 为语雀数据库中的标识号.

```bash
juq repo info {repo_id} [-t Book|Design]
# 指定知识库的信息. type, 类型: 默认为 Book, 以下同
juq repo toc {repo_id}
# 指定知识库的目录结构
juq repo search {q} [-t Book|Design]
# 模糊搜索知识库. q 模糊搜索关键词
juq repo docs {repo_id}
# 指定知识库的全部文档, 不建议使用, toc 指令结果更加丰富.
juq repo create {slug} {name} [-g {group_id}] [-p 0|1|2] [-d {description}]
# 创建知识库.
# slug: 路径名; name: 知识库名;
# group_id: 若该知识库将属于某团队, 使用该参数并配置即可;
# p, public: 0 为私密, 1 为仅对登录用户开放, 2 为对所有人开放;
# description: 知识库描述
juq repo update {repo_id} [-s {slug}] [-n {name}] [-p 0|1|2] [-d {description}]
# 更新知识库信息. 参数同上.
juq repo delete {repo_id}
# 删除知识库.
```

#### Doc

文档的唯一标识为{repo_id} 和({slug} 或 {id}), **但 {slug} 不支持大部分接口, 因此强烈要求仅使用 {id}**

```bash
juq doc info {repo_id} {id}
# 查看文档信息
juq doc toc {repo_id} {id} [-b {before}]|[-a {after}] [-d {depth}]
# 修改文档在知识库中的目录位置.
# b, before: 指定在某文档之前, 使用 {id} 指定;
# a, after: 指定在某文档之后;
# after, before 参数二选一, 或可以都不设置, 默认添加在知识库的末尾.
# d, depth: 文档的深度.
# 如 $juq doc toc inhzus/book 232435 -b 232434 -d 1
juq doc create {repo_id} {file} [-s {slug}] [-t {title}] [-p 0|1]
# 上传本地 markdown 文档.
# file: 本地 markdown 文件的位置, 其中图片将自动上传;
# slug: 文档路径名, 默认为随机串;
# title: 文档名, 默认为文件名;
# p, public, 使用该参数即公开, 默认私密.
# 如: $juq doc create inhzus/book doc.md -s test_doc -t "test documentation" -p
juq doc update {repo_id} {id} {file} [-s {slug}] [-t {title}] [-p 0|1]
# 使用本地 markdown 更新文档, 参数同上.
juq doc delete {repo_id} {id}
# 删除文档.
```

## Yuque SDK

本项目也是"语雀" 的 SDK.

### Installation

```bash
pip3 install juq
```

### Configuration

配置信息有: 

```python
API_BASE_URL = 'https://www.yuque.com/api/v2'
TIMEOUT = 5
SERIALIZE = True
TOKEN = ''
```

其中 `API_BASE_URL` 为 API 路径, 若为企业用户需要参考文档设置.

TIMEOUT 为请求 API 延迟.

SERIALIZE 为是否序列化结构, 默认 True, 方便 type hints. 在当作 SDK 使用时, 为了避免 API 变动导致序列化丢失信息, 非常建议设为 False.

TOKEN 为 Personal Access Token.

配置方法参考 [上文](#config).

当然, 也可以在代码中进行配置, 只要在 SDK 调用前设置即可, 如

```python
from juq import config
from juq import user_handler

config['SERIALIZE'] = False
print(user_handler.get_user_info_anonymous('inhzus'))
```

### Notice

User, Group, Book/Repo, Doc 有不同的识别序列.

User 的唯一标识为 {login} 或 {id}. {login} 即用户路径名, {id} 为语雀数据库中的标识号.

Group 同上.

Book 的唯一标识为 ({login}|{id})/{slug} 或 {id}, 其中, {login} 和 {id} 是 User 或 Group 的标识, {slug} 为 Book 路径名, {id} 为语雀数据库中的标识号.

Doc 的唯一标识为{repo_id} 和({slug} 或 {id}), **但 {slug} 不支持大部分接口, 因此强烈要求仅使用 {id}**

### Usage

配置文件请 `from juq import config` 进行配置.

 `from juq import user_handler, group_handler, repo_handler, doc_handler` 分别对应 API [文档](https://www.yuque.com/yuque/developer/api)

详细使用说明请查看 docstring 或直接参考 API 文档传入参数即可.

