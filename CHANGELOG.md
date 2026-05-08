# Changelog

## Unreleased

No unreleased changes yet.

## v0.1.1 - 2026-05-08

- Improved local README link handling for targets with fragments or query strings, such as `CHANGELOG.md#v011---2026-05-08`.
- Ignored non-file links such as `mailto:` and `tel:` to reduce false positives.
- Added regression tests for local link normalization.

## v0.1.0 - 2026-04-22

- Initial CLI for roasting README drift and reporting missing local paths.
- Added roast, review, json, and strict output modes.
- Added support for checking custom README file names such as `README.zh-CN.md`.
- Added English and Chinese README documentation.
