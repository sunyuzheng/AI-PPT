# AI-PPT

AI-PPT is a lightweight Python project that helps you turn a short textual
outline into a structured presentation plan. The package ships with a CLI that
can be extended to plug in LLM powered generators or PowerPoint exporters.

## Getting started

### Prerequisites

- Python 3.9+
- (Optional) A virtual environment

### Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

### Usage

You can pass outline entries directly on the command line:

```bash
ai-ppt "Quarterly Review" \
  "Introduction: Project scope; Objectives" \
  "Results" \
  "Next steps: Hiring plan; Budget" 
```

Or read them from a text file (one entry per line):

```bash
ai-ppt "Quarterly Review" --file outline.txt
```

Each outline entry may contain a colon (`:`). The text before the colon becomes
the slide title while the right-hand side is split into bullet points using
semi-colons (`;`). Entries without a colon become bullet-free slides.

### Running tests

```bash
pytest
```

## Project structure

- `src/ai_ppt/main.py` – core logic and CLI entry point.
- `tests/` – unit tests for critical functionality.

## License

This project is released under the MIT license.
