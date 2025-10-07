import pytest

from ai_ppt.main import PresentationPlan, Slide, generate_presentation, parse_outline_item


def test_parse_outline_item_with_bullets():
    title, bullets = parse_outline_item("Intro: Goal; Agenda")
    assert title == "Intro"
    assert bullets == ["Goal", "Agenda"]


def test_parse_outline_item_without_bullets():
    title, bullets = parse_outline_item("Summary")
    assert title == "Summary"
    assert bullets == []


def test_generate_presentation_creates_slides():
    plan = generate_presentation("Demo", ["Intro: Goal", "Summary"])
    assert isinstance(plan, PresentationPlan)
    assert plan.title == "Demo"
    assert len(plan.slides) == 2
    assert plan.slides[0] == Slide(title="Intro", bullet_points=["Goal"])
    assert plan.slides[1] == Slide(title="Summary", bullet_points=[])


def test_generate_presentation_requires_outline():
    with pytest.raises(ValueError):
        generate_presentation("Empty", [])
