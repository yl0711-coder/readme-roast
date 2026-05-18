# README Roast v0.1.1

This maintenance release reduces false positives when checking README links.

## Changed

- Improved local README link handling for targets with fragments or query strings.
- Ignored non-file links such as `mailto:` and `tel:`.

## Fixed

- Added regression coverage for local link normalization.
- Updated `readme_roast.__version__` to `0.1.1` so runtime metadata matches the package version and release tag.

## Validation

- Unit tests passed.
- Source compilation passed.
- CLI import/version check passed.
