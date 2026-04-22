# README Roast

[English](README.md) | [简体中文](README.zh-CN.md)

## 一句话定位

像一个嘴很毒的 reviewer 一样吐槽 README 漂移问题，或者切到严格模式，把吐槽变成可执行检查。

## 为什么做这个

很多仓库的 README 写得很自信，但和实际代码已经不是一回事：

- 安装步骤过时
- 文档里的路径不存在
- 目录结构示例早就漂移了
- README 和真实仓库状态脱节

README Roast 把这个问题做成一个本地可运行的小工具。

## MVP

- 检测 README 本地 Markdown 链接是否指向不存在的文件
- 检测明显的反引号路径是否存在
- 检测 README 里的项目树目录项是否存在
- 输出吐槽模式结果
- 输出严格模式结果

## 状态

当前版本：`v0.1.0`

第一版范围：

- 只检查本地 README 路径真实性
- 不访问网络
- 不检查远程链接
- 暂不做包管理器元数据检查
- 不自动修复

## 使用

```bash
bin/readme-roast
bin/readme-roast --mode review
bin/readme-roast --json
bin/readme-roast --strict
bin/readme-roast /path/to/repo --mode review --strict
```

退出码：

- `0`：命令执行成功
- `1`：`--strict` 模式下发现问题
- `2`：输入无效，例如缺少 `README.md`

## 检查内容

- 本地 Markdown 链接，例如 `[Changelog](CHANGELOG.md)`
- 明显的反引号路径，例如 `` `scripts/dev.py` ``
- README 代码块中的项目树条目

## 适合的技术形态

- Python
- 单一 CLI
- 无网络依赖

## 非目标

- 完整 Markdown 解析器
- HTTP 链接检查器
- 包管理器元数据验证器
- 自动修复 README 漂移

## 第一批演示场景

拿那些 README 和实际结构不一致的仓库去跑，输出：

- 一张吐槽模式截图
- 一张严格模式截图

## 开发

```bash
PYTHONPATH=src python -m unittest discover -s tests
bin/readme-roast --mode review --strict
```
