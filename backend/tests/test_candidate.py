from models.candidate import Candidate

candidate = Candidate(
    id="C-01",
    title="Warfarin-NSAID Interaction",
    type="CONSTRAINT",

    content_full="Full content",
    content_compressed="Compressed content",
    content_constraint_only="Constraint only content",

    retrieval_weight=0.98,
    injection_weight=0.95,

    distance_from_entry=4,

    zone=2,

    tokens_full=85,
    tokens_compressed=22,
    tokens_constraint_only=8
)

print(candidate)