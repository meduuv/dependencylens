# DependencyLens

> Dependency metadata inspection helpers for Python projects.

[![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?style=flat-square)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-111111?style=flat-square)](LICENSE)

DependencyLens is a small, dependency-free library for inspecting and normalizing Python dependency declarations.

## Features

- Parse dependency requirement strings
- Extract package names
- Group entries by package name
- Detect duplicate package entries
- Dependency-free runtime
- Simple Python API

## Installation

```bash
pip install dependencylens
```

## Example

```python
from dependencylens import extract_package_name

name = extract_package_name("requests>=2.31,<3")
print(name)
```

Use the package's public API and type signatures for the complete set of supported helpers.

## Design

DependencyLens deliberately focuses on **metadata inspection**, not package installation or environment mutation.

```text
requirement strings
        ↓
    parse / normalize
        ↓
 structured metadata
        ↓
   your tooling
```

This makes it suitable as a building block for dependency audits, project analysis and release tooling.

## Development

```bash
python -m pytest
```

## License

MIT. See [`LICENSE`](LICENSE).

Built by **Meduuv**.

[More projects](https://github.com/meduuv?tab=repositories) · [guns.lol/meduu](https://guns.lol/meduu)
