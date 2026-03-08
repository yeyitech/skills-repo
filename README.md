# skills-repo

这是一个公开的 Skill 仓库，用来集中维护可复用的 Skills，并提供尽量简单的安装方式。

目标是让用户可以：

- 通过 GitHub 公开仓库获取 Skill
- 通过一条命令完成安装
- 自动把 Skill 复制到本地可识别的 skills 目录
- 方便后续更新、覆盖安装和批量安装

## 快速开始

### 方式一：先安装安装器，再安装 Skill

如果你希望以后持续安装、更新 Skill，推荐先安装一个本地安装器命令。

安装安装器：

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/yeyitech/skills-repo/main/bootstrap.sh)
```

默认会安装到：

```bash
~/.local/bin/yeyitech-skills
```

安装完成后可以直接使用：

```bash
yeyitech-skills --list
yeyitech-skills --skill generate-alipay-wechat-report
yeyitech-skills --all
```

这个本地安装器会自动：

1. 把仓库同步到本地缓存目录
2. 在需要时更新缓存
3. 把指定 Skill 复制到本地可识别的 skills 目录

### 方式二：一条命令直接安装

如果你只是想快速安装某个 Skill，可以直接执行：

安装单个 Skill：

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/yeyitech/skills-repo/main/install.sh) \
  --skill generate-alipay-wechat-report
```

安装全部 Skill：

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/yeyitech/skills-repo/main/install.sh) \
  --all
```

## 缓存目录

默认仓库缓存目录：

```bash
~/.cache/yeyitech/skills-repo
```

也可以自定义缓存目录：

```bash
SKILLS_REPO_CACHE_DIR=~/project/cache/skills-repo \
  bash <(curl -fsSL https://raw.githubusercontent.com/yeyitech/skills-repo/main/install.sh) \
  --skill generate-alipay-wechat-report
```

## 从本地仓库安装

如果你已经把仓库 clone 到本地，也可以直接调用本地安装脚本。

```bash
git clone https://github.com/yeyitech/skills-repo.git
cd skills-repo
python3 scripts/install_skill.py --skill generate-alipay-wechat-report
```

安装全部 Skill：

```bash
python3 scripts/install_skill.py --all
```

查看可用 Skill：

```bash
python3 scripts/install_skill.py --list
```

覆盖已安装的同名 Skill：

```bash
python3 scripts/install_skill.py --skill generate-alipay-wechat-report --force
```

## 目标目录规则

安装器会扫描这些常见的本地 skills 目录：

- `~/.agents/skills`
- `~/.codex/skills`
- `~/.claude/skills`
- `~/.config/claude/skills`

规则如下：

- 如果上述目录里已有一个或多个存在，就把选中的 Skill 复制到所有已存在的目录里
- 如果一个都不存在，就默认创建 `~/.agents/skills` 并安装进去
- 如果你想手动指定目录，可以使用 `--target`

安装到自定义目录示例：

```bash
python3 scripts/install_skill.py \
  --skill generate-alipay-wechat-report \
  --target ~/.codex/skills
```

## 当前收录的 Skills

- `infographic-image/`：信息图与视觉长图生成 Skill 源码
- `infographic-image.skill`：打包后的分发文件
- `agent-harness-engineering/`：Agent 工程化脚手架 Skill 源码
- `agent-harness-engineering.skill`：打包后的分发文件
- `generate-alipay-wechat-report/`：支付宝 / 微信原生账单数字报表 Skill 源码
- `generate-alipay-wechat-report.skill`：打包后的分发文件

## 安装相关文件

- `bootstrap.sh`：先安装本地安装器命令
- `install.sh`：一次性安装入口
- `scripts/install_skill.py`：实际执行安装与复制的脚本

## 说明

- 这个仓库本质上是一个公开 GitHub 仓库
- 安装的本质是：把 Skill 从仓库复制到本地可识别的 skills 目录
- 仓库缓存的作用是为了后续更新更方便，不需要每次都重新手动 clone
