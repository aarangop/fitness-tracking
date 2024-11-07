import pytest
from utils import parse_obsidian_metadata


@pytest.fixture
def temp_note_with_metadata(tmp_path):
    content = """---
title: Test Note
tags: [tag1, tag2]
measurements:
  - weight: 70
  - height: 180
---
# Note content"""
    note_path = tmp_path / "test_note.md"
    with open(note_path, "w") as f:
        f.write(content)
    return str(note_path)


@pytest.fixture
def temp_note_empty_metadata(tmp_path):
    content = """---
---
# Note content"""
    note_path = tmp_path / "empty_metadata.md"
    with open(note_path, "w") as f:
        f.write(content)
    return str(note_path)


@pytest.fixture
def temp_note_invalid_yaml(tmp_path):
    content = """---
title: Test Note
tags: [tag1, tag2
---
# Note content"""
    note_path = tmp_path / "invalid_yaml.md"
    with open(note_path, "w") as f:
        f.write(content)
    return str(note_path)


def test_parse_metadata_with_arrays(temp_note_with_metadata):
    metadata = parse_obsidian_metadata(temp_note_with_metadata)
    assert metadata["title"] == "Test Note"
    assert metadata["tags"] == ["tag1", "tag2"]
    assert len(metadata["measurements"]) == 2
    assert metadata["measurements"][0]["weight"] == 70
    assert metadata["measurements"][1]["height"] == 180


def test_parse_empty_metadata(temp_note_empty_metadata):
    metadata = parse_obsidian_metadata(temp_note_empty_metadata)
    assert metadata == {}


def test_parse_invalid_yaml(temp_note_invalid_yaml):
    metadata = parse_obsidian_metadata(temp_note_invalid_yaml)
    assert metadata == {}


def test_parse_nonexistent_file():
    metadata = parse_obsidian_metadata("nonexistent_file.md")
    assert metadata == {}
