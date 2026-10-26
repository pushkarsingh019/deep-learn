# PROTOTYPE — Deep Learn feedback flow

This throwaway logic prototype asks whether automatic lesson snapshots combined with explicit feedback actions produce a state model that feels private, understandable, and useful for future supervised fine-tuning and preference optimization. It has no persistence and does not touch the learning vault or feedback directory.

From the profile repository root, run it with one command:

```bash
python3 skills/deep-learn/prototypes/feedback-flow-prototype/feedback_prototype.py
```

To replay the built-in example:

```bash
python3 skills/deep-learn/prototypes/feedback-flow-prototype/feedback_prototype.py --demo
```

The pure state transitions are isolated in `feedback_logic.py`; the terminal shell exists only to make the transitions tangible.
