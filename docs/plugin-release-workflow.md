# Evidencecraft 三平台插件维护与发布

本文记录 Evidencecraft 在 Claude Code、Codex 与 OpenClaw/ClawHub 上已经验证成功的打包、安装、
更新和远端发布方式。它是维护者流程，不限定 Skill 数量；任何未来 Skill 都使用同一套门。

## 1. 单一 Skill 源与三个分发入口

```text
evidencecraft/
├── package.json                            # ClawHub bundle identity/version；无 runtime
├── openclaw.plugin.json                    # OpenClaw 声明式 Skill bundle manifest；无 entrypoint
├── .agents/plugins/marketplace.json       # Codex repo marketplace
├── .codex-plugin/plugin.json              # Codex manifest
├── .claude-plugin/
│   ├── plugin.json                        # Claude Code manifest
│   └── marketplace.json                   # Claude Code repo marketplace
└── skills/                                # 三个平台共用的唯一生产 Skill 源
    └── <skill-name>/SKILL.md
```

Claude Code 与 Codex 从根目录 `skills/` 加载 Skill。ClawHub 当前的 bundle 发布器要求
`openclaw.plugin.json`；Evidencecraft 用它只声明 `skills: ["./skills"]`、空配置 Schema 和版本，
让 OpenClaw 把根 `skills/` 映射为普通 Skills。该 manifest 没有 JavaScript entrypoint、runtime、
hooks 或工具注册，因此仍是 skills-only bundle，也不需要复制的 OpenClaw Skill 树。

根 `package.json` 只提供 ClawHub bundle 的稳定 scoped name、semver、来源和许可证，不声明
`openclaw.extensions`，不执行安装脚本，也不会把 bundle 变成 native code plugin。

新增 Skill 只新增 `skills/<skill-name>/` 及其实际配套，不建立 `skills-claude/`、
`skills-codex/` 或 `skills-openclaw/`。Skill 内的 `agents/openai.yaml` 是 Codex 展示元数据；其他
Harness 会随 bundle 携带但仍以 `SKILL.md` 作为 Skill 定义。

当前 Claude 结构借鉴 Superpowers：Claude manifest 只承载 Claude 元数据，依靠默认目录发现
`skills/`；Claude marketplace entry 使用 `source: "./"`。Evidencecraft 是按自然任务触发的
skills-only/bundle plugin，不需要为了形式同构增加 hooks。未来只有出现经过验证的跨会话启动需求
时，才单独设计 hooks。

## 2. 两个不同的门

### Release-readiness gate

任何 Skill 新增、修改、重命名或删除都必须通过；不需要发布授权：

1. 按 `docs/skill-evaluation-policy.md` 验证实际行为变化；
2. 运行受影响 Skill 的 `quick_validate.py`、链接检查和 `git diff --check`；
3. 运行 Codex plugin validator；
4. 运行 `claude plugin validate --strict .`；
5. 运行 `clawhub package validate .`，确认 family 为 `bundle-plugin` 且 Skill roots 完整；
6. 从临时 Git commit 安装三个候选，比较安装缓存与源码的整个 `skills/` 目录；
7. 动态检查当前 Skill 集，不断言固定数量；
8. 确认没有未解析占位符、凭证、本机绝对路径、`reports/`、`evals/`、transcript 或 raw logs
   进入候选包。

通过此门只说明改动可以发布。没有用户明确的 `release`/`push` 授权时：

- 不 bump 版本；
- 不创建 release commit、tag、GitHub Release 或 ClawHub release；
- 不推送远端；
- 在交付结果中报告建议的 semver 级别和仍未发布的状态。

### Release/push gate

只有用户明确要求发布或推送后执行。不得把“完成 Skill”“保持可发布”或“更新插件兼容性”推断为
远端发布授权。

## 3. Semver 与版本锁步

建议按以下规则选择版本：

- patch：修正文案、Trigger 边界、停止纪律、模板或实现缺陷，不新增对外职责；
- minor：新增 Skill、增加向后兼容的工作流能力、支持新 Harness；
- major：在 `1.0.0` 后改变 plugin/Skill namespace、移除公开 Skill、破坏稳定调用或产物接口；
- `0.x` 阶段如有破坏性变化，至少增加 minor，并在 Release notes 明确迁移方式。

发布版本必须锁步：

| 位置 | 字段 |
|---|---|
| `.codex-plugin/plugin.json` | `.version` |
| `.claude-plugin/plugin.json` | `.version` |
| `.claude-plugin/marketplace.json` | 对应 plugin entry 的 `.version` |
| `openclaw.plugin.json` | `.version` |
| `package.json` | `.version` |
| `README.md` | Claude/Codex 固定 tag 与 ClawHub 固定版本示例 |
| Git | annotated tag `vX.Y.Z` |
| ClawHub | bundle package release `X.Y.Z`，`latest` 指向该版本 |

`.agents/plugins/marketplace.json` 没有版本字段。不要为“统一”自行添加。

可用下列检查防止版本漂移：

```bash
release_version="X.Y.Z"
test "$(jq -r .version .codex-plugin/plugin.json)" = "$release_version"
test "$(jq -r .version .claude-plugin/plugin.json)" = "$release_version"
test "$(jq -r '.plugins[] | select(.name == "evidencecraft") | .version' \
  .claude-plugin/marketplace.json)" = "$release_version"
test "$(jq -r .version openclaw.plugin.json)" = "$release_version"
test "$(jq -r .version package.json)" = "$release_version"
```

Claude Code strict validator 与真实安装均已验证在 Claude manifest 和 marketplace entry 同时记录
版本的形状，因此两处必须锁步。ClawHub bundle 版本通过发布命令指定，不在 Skills 中加入独立
版本；这样整套插件保持一个 release line。

## 4. 候选包验证

Git-backed marketplace 安装已提交的 Git 快照，不读取未提交工作树。发布前把候选复制到临时目录，
排除 `.git/`、`reports/`、运行产物和系统垃圾文件，在临时目录创建一次 Git commit，再让三个
安装器从该快照安装。不要用源码目录的成功加载代替候选快照验证。

验证当前完整 Skill 集时使用目录比较，而不是固定数量：

```bash
find skills -mindepth 2 -maxdepth 2 -name SKILL.md -print | sort
diff -qr skills <installed-path>/skills
```

Codex 候选验证至少包括：

```bash
python3 /path/to/current/plugin-creator/scripts/validate_plugin.py .
codex plugin marketplace add /path/to/temporary/git-repository
codex plugin add evidencecraft@evidencecraft
```

Claude Code 候选验证至少包括：

```bash
claude plugin validate --strict .
claude plugin marketplace add /path/to/temporary/git-repository
claude plugin install evidencecraft@evidencecraft --scope user
```

OpenClaw 候选验证使用隔离 state/config，不污染用户正在运行的 Gateway：

```bash
clawhub package validate /path/to/temporary/git-repository --out /tmp/inspector-report
OPENCLAW_STATE_DIR=/tmp/evidencecraft-openclaw \
OPENCLAW_CONFIG_PATH=/tmp/evidencecraft-openclaw/openclaw.json \
  openclaw plugins install /path/to/temporary/git-repository
OPENCLAW_STATE_DIR=/tmp/evidencecraft-openclaw \
OPENCLAW_CONFIG_PATH=/tmp/evidencecraft-openclaw/openclaw.json \
  openclaw plugins inspect evidencecraft
```

安装后用 fresh context 调用至少一个受影响入口，并验证最近邻边界或交接。Claude Code 的显式
Skill 语法是 `/evidencecraft:<skill-name>`；Codex 的显式语法是
`$evidencecraft:<skill-name>`。OpenClaw bundle Skills 使用普通 Skill 发现与调用，不假设 Claude/
Codex namespace。路由测试必须明确 Plan 已绑定的选择，例如 sequential 或 multi-agent Executor；
若输入没有该选择，Skill 停止并索取上下文是正确行为，不应为了让测试返回唯一 Skill 而修改生产
规则。

## 5. 公开仓库的双历史策略

本仓库有意保留两条本地分支：

- `main`：本地开发历史；可能包含不适合公开的旧大型评测历史，因此不得直接推到 origin；
- `public-main`：精简公开历史，跟踪 `origin/main`，只包含已审计的发布 tree。

发布前先确认远端没有超前或分叉：

```bash
test "$(git branch --show-current)" = "main"
git fetch origin
test "$(git rev-parse public-main)" = "$(git rev-parse origin/main)"
```

同时确认目标 tag 在本地和远端都不存在；若已存在，停止并选择新版本，不移动已发布 tag：

```bash
release_version="X.Y.Z"
test -z "$(git tag --list "v${release_version}")"
test -z "$(git ls-remote --tags origin "refs/tags/v${release_version}*")"
```

先显式暂存发布文件，不使用宽泛的 `git add -A`。提交前审阅 `git status --short`、完整 staged
diff、`git diff --cached --check` 和敏感内容扫描，并断言 staged paths 不含 `reports/`、`evals/`
或 routine logs。确认后把已验证改动提交到本地 `main`。

然后让公开 release commit 使用同一 tree、以旧 `public-main` 为唯一父提交：

```bash
release_version="X.Y.Z"
public_parent=$(git rev-parse public-main)
release_tree=$(git rev-parse main^{tree})
public_commit=$(git commit-tree "$release_tree" \
  -p "$public_parent" \
  -m "feat: release Evidencecraft v${release_version}")

git branch -f public-main "$public_commit"
git diff --exit-code main^{tree} public-main^{tree}
test "$(git rev-parse public-main^)" = "$public_parent"
git tag -a "v${release_version}" public-main \
  -m "Evidencecraft v${release_version}"
```

只有 release/push 已获明确授权且上述检查通过，才能 fast-forward 推送：

```bash
git push origin public-main:main
git push origin "v${release_version}"
```

不要 force-push `origin/main`，不要把本地 `main` 推为公开 `main`，也不要以恢复旧历史的方式构造
发布。推送后使用 `git ls-remote` 核对 `origin/main` 和 tag 解引用 SHA 都指向 `public-main`。

## 6. GitHub tag 与 ClawHub 发布

最终验收必须从远端 tag 重新开始，不能复用本地候选缓存。

Codex 固定 tag 安装：

```bash
codex plugin marketplace add dufeiyang123/evidencecraft --ref "vX.Y.Z"
codex plugin add evidencecraft@evidencecraft
```

Claude Code 固定 tag 安装：

```bash
claude plugin marketplace add dufeiyang123/evidencecraft@vX.Y.Z
claude plugin install evidencecraft@evidencecraft --scope user
```

ClawHub 首次发布需要独立于 `gh` 的登录：

```bash
npm install -g clawhub
clawhub login
clawhub whoami
```

先从不可变 GitHub tag dry-run，再正式发布相同来源和版本：

```bash
clawhub package publish dufeiyang123/evidencecraft@vX.Y.Z \
  --family bundle-plugin \
  --owner dufeiyang123 \
  --name @dufeiyang123/evidencecraft \
  --display-name Evidencecraft \
  --version X.Y.Z \
  --tags latest \
  --dry-run

clawhub package publish dufeiyang123/evidencecraft@vX.Y.Z \
  --family bundle-plugin \
  --owner dufeiyang123 \
  --name @dufeiyang123/evidencecraft \
  --display-name Evidencecraft \
  --version X.Y.Z \
  --tags latest \
  --wait
```

正式发布后从 ClawHub 安装：

```bash
openclaw plugins install clawhub:@dufeiyang123/evidencecraft@X.Y.Z
openclaw plugins inspect evidencecraft
```

最后检查：

- 三边解析出的版本都是 `X.Y.Z`；
- 安装缓存中的完整 `skills/` 与 tag 源码一致；
- 所有当前 Skill 都能被发现，不以某个历史数量为通过条件；
- 至少一个 fresh-context 入口调用通过；
- 远端公开 tree 与 ClawHub bundle 不含 `reports/`、`evals/`、transcript、凭证或本机路径；
- `origin/main`、annotated tag 解引用和本地 `public-main` 指向同一 release commit；
- GitHub 与 ClawHub 保持预期可见性、来源和许可证。

需要正式对外发布时，基于已经推送的 tag 创建 GitHub Release，并在 notes 中记录新增能力、安装
命令、兼容性和迁移要求。ClawHub changelog 使用同一份紧凑摘要。routine 验证证据保留在任务
结果或 release notes，不把 raw logs 重新提交到仓库。

Release notes 至少记录：实际变更的 Skill/包装能力、semver 理由、三个 validator 结果、三个
Harness 的安装结果、迁移或已知限制。Skill 列表从实际 diff/目录生成，不维护固定清单。

## 7. 用户更新路径

跟踪默认分支的 Codex 用户：

```bash
codex plugin marketplace upgrade evidencecraft
codex plugin add evidencecraft@evidencecraft
```

跟踪默认分支的 Claude Code 用户：

```text
/plugin marketplace update evidencecraft
/plugin update evidencecraft@evidencecraft
/reload-plugins
```

跟踪 ClawHub `latest` 的 OpenClaw 用户：

```bash
openclaw plugins update evidencecraft
openclaw gateway restart
```

Codex 更新后启动新 thread；Claude Code 执行 `/reload-plugins` 或重启；OpenClaw 重启 Gateway 或
进入新 session。固定 Git tag 或 ClawHub exact version 的用户不会自动越过固定版本，必须显式切换
到新版本。
