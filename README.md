# README Roast

[English](README.md) | [简体中文](README.zh-CN.md)

## One-Line Idea

Roast a repository README like a mean reviewer, or switch to strict mode and turn the jokes into actionable checks.

## Why It Exists

Many repositories have README files that sound confident but drift away from reality:

- install steps no longer work
- paths in the docs do not exist
- repository structure examples are outdated
- package metadata and README disagree

This project turns that pain into a fun local tool.

## Core Modes

- `roast`: funny output
- `review`: serious output
- `strict`: CI-friendly failure mode

## MVP

- detect local README links that point to missing files
- detect obvious referenced paths that do not exist
- detect project tree snippets that mention missing directories
- output funny roast lines
- output strict machine-readable findings

## Status

Current version: `v0.1.1`

First version scope:

- local README path truth-checking only
- no network access
- no remote link validation
- no package-manager-specific checks yet
- no automatic fixes

Version `v0.1.1` also understands local links with fragments or query strings, such as `CHANGELOG.md#v011---2026-05-08`, and ignores non-file links such as `mailto:`.

## Good Fit

- Python
- single CLI
- no network

## Non-Goals

- full Markdown parser with every edge case
- remote HTTP link checker
- full package manager validation replacement

## First Demo

Run it against intentionally messy repositories and produce:

- a roast screenshot
- a strict report screenshot

## Requirements

- Python 3.9 or later
- No network access and no third-party runtime dependency

## Installation

Run directly from a clone:

```bash
bin/readme-roast
```

Or install the package locally if your Python environment has packaging tools available:

```bash
python -m pip install -e .
readme-roast --mode review
```

## Usage

```bash
bin/readme-roast
bin/readme-roast --mode review
bin/readme-roast --json
bin/readme-roast --strict
bin/readme-roast --readme README.zh-CN.md --mode review
bin/readme-roast /path/to/repo --mode review --strict
```

Exit codes:

- `0`: command ran successfully
- `1`: findings present in `--strict` mode
- `2`: invalid input such as missing `README.md`

## Example Output

Roast mode against a README that drifted from its repository:

```text
README Roast

Verdict:
- this README believes in folders that no longer exist
- findings: 5
- confidence without evidence: 47%
- documentation drama: 90%
- maintenance aura: optimistic chaos

Highlights:
- line 3: local link target "docs/guide.md" does not exist
- line 3: local link target "CHANGELOG.md" does not exist
- line 5: referenced path "scripts/dev.sh" does not exist
- line 9: project tree entry "src/" does not exist
- line 10: project tree entry "missing_dir/" does not exist

Advice:
- open the README and the repository side by side
- remove claims that no longer exist
- make the docs slightly less ambitious than the code
```

The same drift in `--mode review --strict` (CI-friendly, exits `1`):

```text
README Review

Findings:
- line 3 [link] local link target "docs/guide.md" does not exist
- line 3 [link] local link target "CHANGELOG.md" does not exist
- line 5 [path] referenced path "scripts/dev.sh" does not exist
- line 9 [tree] project tree entry "src/" does not exist
- line 10 [tree] project tree entry "missing_dir/" does not exist

Result: failed
```

## What It Checks

- local Markdown links such as `[Changelog](CHANGELOG.md)`
- local Markdown links with anchors such as `[Changelog](CHANGELOG.md#v011---2026-05-08)`
- obvious inline path references such as `` `scripts/dev.py` ``
- project tree entries inside README code blocks

## Development

```bash
PYTHONPATH=src python -m unittest discover -s tests
bin/readme-roast --mode review --strict
```

## License

MIT
