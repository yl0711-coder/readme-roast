# v0.1.0

Initial public release of README Roast.

## Added

- CLI for detecting local README drift
- Checks for missing local Markdown links
- Checks for missing inline path references
- Checks for missing project tree entries in README examples
- `roast` mode for playful output
- `review` mode for strict human-readable output
- `--json` output for tooling
- `--strict` for CI use
- `--readme` support for custom README files such as `README.zh-CN.md`
- English and Chinese README
- GitHub Actions workflow

## Verified

- Unit tests passed
- Clean repository self-check passed
- Dirty sample repository correctly reported missing local links, inline paths, and tree entries

## Positioning

README Roast is intentionally small. It does not try to validate remote links, parse every Markdown edge case, or replace package-manager-specific validation tools. It focuses on one thing: whether a repository README still matches local reality.
