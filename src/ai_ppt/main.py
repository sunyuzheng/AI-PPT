"""Core helpers for the AI-PPT project.

The module exposes a small utility that converts a lightweight outline into a
structured representation that can later be used to feed LLMs or tooling that
builds PowerPoint files.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Sequence, Tuple


@dataclass
class Slide:
    """Description of a single presentation slide."""

    title: str
    bullet_points: List[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        title = self.title.strip()
        if not title:
            raise ValueError("Slide title must not be empty")
        self.title = title

        sanitized: List[str] = []
        for bullet in self.bullet_points:
            cleaned = bullet.strip()
            if not cleaned:
                raise ValueError("Bullet points must not be empty strings")
            sanitized.append(cleaned)
        self.bullet_points = sanitized


@dataclass
class PresentationPlan:
    """High-level structure of a presentation."""

    title: str
    slides: List[Slide]

    def __post_init__(self) -> None:
        title = self.title.strip()
        if not title:
            raise ValueError("Presentation title must not be empty")
        if not self.slides:
            raise ValueError("Provide at least one slide in the outline")
        self.title = title


def parse_outline_item(item: str) -> Tuple[str, List[str]]:
    """Parse a single outline row.

    The helper accepts free-form outline strings. If the string contains a
    colon (":"), the portion to the left is treated as the slide title while
    the right-hand side is split into bullet points using semi-colons.

    Examples
    --------
    >>> parse_outline_item("Introduction: Goals; Agenda")
    ('Introduction', ['Goals', 'Agenda'])
    >>> parse_outline_item("Summary")
    ('Summary', [])
    """

    title, bullet_blob = (item.split(":", 1) + [""])[:2]
    title = title.strip()
    bullets = [bullet.strip() for bullet in bullet_blob.split(";") if bullet.strip()]
    return title, bullets


def generate_presentation(title: str, outline: Sequence[str]) -> PresentationPlan:
    """Create a presentation plan from a sequence of outline entries."""

    slides = []
    for raw_item in outline:
        parsed_title, bullets = parse_outline_item(raw_item)
        slides.append(Slide(title=parsed_title, bullet_points=bullets))

    return PresentationPlan(title=title, slides=slides)


def _read_outline_from_file(file_path: Path) -> List[str]:
    """Read an outline from a text file."""

    with file_path.open("r", encoding="utf-8") as handle:
        lines = [line.strip() for line in handle.readlines()]
    return [line for line in lines if line]


def _resolve_outline(args_outline: Sequence[str], file_path: Path | None) -> List[str]:
    """Resolve the outline from CLI arguments or a file."""

    if file_path:
        return _read_outline_from_file(file_path)
    if args_outline:
        return [item for item in args_outline if item.strip()]
    stdin_content = sys.stdin.read().strip()
    if stdin_content:
        return [line for line in stdin_content.splitlines() if line.strip()]
    raise SystemExit("No outline provided. Pass lines as arguments or via --file.")


def build_parser() -> argparse.ArgumentParser:
    """Return the CLI argument parser."""

    parser = argparse.ArgumentParser(description="Generate an AI-assisted presentation outline")
    parser.add_argument("title", help="Title of the presentation")
    parser.add_argument(
        "outline",
        nargs="*",
        help="Outline entries in the form 'Slide Title: bullet one; bullet two'.",
    )
    parser.add_argument(
        "-f",
        "--file",
        type=Path,
        help="Path to a text file containing outline entries (one per line)",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """CLI entrypoint for generating presentation outlines."""

    parser = build_parser()
    args = parser.parse_args(argv)

    outline = _resolve_outline(args.outline, args.file)
    plan = generate_presentation(args.title, outline)

    for idx, slide in enumerate(plan.slides, start=1):
        print(f"Slide {idx}: {slide.title}")
        for bullet in slide.bullet_points:
            print(f"  - {bullet}")

    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    raise SystemExit(main())
