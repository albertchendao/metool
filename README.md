# 学习工作使用的命令行工具

## 背景

学习和工作中有时候会编写一些 Python 脚本并执行, 这些脚本的保存管理是个问题, 每次找脚本配置 Python 环境然后运行都很麻烦, 
所以干脆集成到单独的一个命令行工具. 因为 PyPi 中已经有 mytool 包了, 所以起名叫 metool

## 迭代流程

1. 修改源码
2. 修改 `pyproject.toml` 中版本号
3. 打包 `poetry build`
4. 发布 `poetry publish`
5. 本地安装 `pip3 install metool --upgrade`

## 测试流程

需要依赖 `pytest`:

```
poetry add pytest --dev
poetry add pytest-repeat --dev
```

在 tests 目录编写测试用例, 然后运行测试:

```
poetry run pytest -s tests/
```

## 可用命令

根据模块划分主命令, 模块下通过子命令执行相应的功能, 例如笔记模块下创建新笔记: `notebook new "测试""`.

### 笔记模块

我使用 Markdown 编写笔记, 所有文档收集到一个 notebook 文件夹, 这个模块命令主要是为了方便创建新文档, 并且将部分标记的文档直接复制到 Jekyll 目录, 发布到博客上.

|主命令|命令|含义|
|----|----|----|
|notebook|ukey|生成笔记所使用的唯一 UUID|
|notebook|udate|生成笔记所使用的随机日期|
|notebook|new|根据模板生成新笔记文档|
|notebook|deploy|复制部分标签笔记文档到 jekyll 也即发布博客 |