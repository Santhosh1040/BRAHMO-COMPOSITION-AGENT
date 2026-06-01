from models.candidate import Candidate
from models.block import Block
from composition.context_builder import build_context


constraint = Candidate(
    id="C-01",
    title="Warfarin Rule",
    type="CONSTRAINT",

    content_full="No NSAIDs with Warfarin",
    content_compressed="Avoid NSAIDs",
    content_constraint_only="NSAID Ban",

    retrieval_weight=0.95,
    injection_weight=0.95,

    distance_from_entry=1
)

decision = Candidate(
    id="D-01",
    title="Paracetamol First",
    type="DECISION",

    content_full="Use Paracetamol before stronger medication",
    content_compressed="Use Paracetamol first",
    content_constraint_only="Paracetamol",

    retrieval_weight=0.80,
    injection_weight=0.85,

    distance_from_entry=2
)

decision.compression_level = "COMPRESSED"

block_constraints = Block(
    id=2,
    name="Global Constraints",
    candidates=[constraint]
)

block_decisions = Block(
    id=3,
    name="Recent Decisions",
    candidates=[decision]
)

context = build_context(
    [
        block_constraints,
        block_decisions
    ]
)

print(context)