# DependencyLens

> Inspect Python dependency declarations without adding runtime dependencies.

DependencyLens is a small utility for extracting and organizing dependency metadata from Python project requirements.

## Why it exists

Dependency files are often the first place to look when reviewing a Python project. DependencyLens keeps that inspection lightweight and scriptable.

## Features

- Parse dependency requirement strings
- Extract package names
- Group entries by package name
- Detect duplicate package declarations
- Zero runtime dependencies

## Example

```python
from dependencylens import parse

result = parse(["requests>=2.0", "httpx==0.27"])
print(result)
```

See the source and tests for the exact supported API.

## Development

```bash
python -m pytest
```

## License

MIT. See `LICENSE`.

## Author

Built by **Medu** · https://guns.lol/meduu