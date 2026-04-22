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

Current version: `v0.1.0`

First version scope:

- local README path truth-checking only
- no network access
- no remote link validation
- no package-manager-specific checks yet
- no automatic fixes

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

## Usage

```bash
bin/readme-roast
bin/readme-roast --mode review
bin/readme-roast --json
bin/readme-roast --strict
bin/readme-roast /path/to/repo --mode review --strict
```

Exit codes:

- `0`: command ran successfully
- `1`: findings present in `--strict` mode
- `2`: invalid input such as missing `README.md`

## What It Checks

- local Markdown links such as `[Changelog](CHANGELOG.md)`
- obvious inline path references such as `` `scripts/dev.py` ``
- project tree entries inside README code blocks

## Non-Goals

- full Markdown parsing
- HTTP link checking
- package metadata validation
- auto-fixing documentation drift

## Development

```bash
PYTHONPATH=src python -m unittest discover -s tests
bin/readme-roast --mode review --strict
```
