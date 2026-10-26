from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def text(name: str) -> str:
    return (ROOT / name).read_text()


class DeepLearnContractTests(unittest.TestCase):
    def test_unknown_baseline_starts_at_zero(self):
        combined = text("LESSONS.md") + text("MATH-AND-CODE.md")
        self.assertIn("no evidence means no assumed prerequisite", combined.lower())

    def test_depth_consent_precedes_formalism(self):
        combined = text("LESSONS.md") + text("MATH-AND-CODE.md")
        self.assertIn("before any source equation or formal definition", combined.lower())

    def test_every_symbol_is_explained_before_use(self):
        self.assertIn(
            "every symbol is introduced before it appears in an equation",
            text("MATH-AND-CODE.md").lower(),
        )

    def test_source_survey_is_legwork_not_moc_dump(self):
        curriculum = text("CURRICULUM.md").lower()
        self.assertIn("source survey is legwork", curriculum)
        self.assertNotIn("add a factual **source ledger** to the moc", curriculum)

    def test_moc_puts_current_learning_before_source_support(self):
        formats = text("FORMATS.md")
        self.assertIn("## Now", formats)
        self.assertLess(formats.index("## Now"), formats.index("## Source"))

    def test_first_drafts_are_outline_only_until_evidence(self):
        combined = text("CURRICULUM.md") + text("LESSONS.md")
        self.assertIn("outline-only", combined.lower())
        self.assertIn("first checkpoint", combined.lower())

    def test_notation_table_is_not_mandatory_lesson_scaffolding(self):
        lesson_template = text("FORMATS.md").split("## Lesson", 1)[1]
        self.assertNotIn("| Source symbol |", lesson_template)

    def test_moc_has_a_small_source_summary_not_a_full_inventory(self):
        formats = text("FORMATS.md").lower()
        self.assertIn("one short source summary", formats)
        self.assertIn("source map", formats)

    def test_continuous_prose_is_the_default_teaching_voice(self):
        lessons = text("LESSONS.md").lower()
        self.assertIn("continuous prose is the default", lessons)
        self.assertIn("lists are reserved", lessons)


if __name__ == "__main__":
    unittest.main()
