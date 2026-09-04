import re

_NAME = re.compile(r"^([A-Za-z0-9][A-Za-z0-9_.-]*)")


def package_name(requirement: str) -> str:
    match = _NAME.match(requirement.strip())
    if not match:
        raise ValueError(f"invalid requirement: {requirement!r}")
    return match.group(1).lower()


def duplicate_names(requirements: list[str]) -> list[str]:
    seen: set[str] = set()
    duplicates: list[str] = []
    for item in requirements:
        name = package_name(item)
        if name in seen and name not in duplicates:
            duplicates.append(name)
        seen.add(name)
    return duplicates


def summarize(requirements: list[str]) -> dict[str, object]:
    names = [package_name(item) for item in requirements]
    return {"count": len(names), "unique": len(set(names)), "duplicates": duplicate_names(requirements)}
