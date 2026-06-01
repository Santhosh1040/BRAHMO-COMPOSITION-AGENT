from models.candidate import Candidate
from composition.compressor import assign_compression_level


constraint_node = Candidate(
    id="C-01",
    title="Warfarin Rule",
    type="CONSTRAINT",

    content_full="full",
    content_compressed="compressed",
    content_constraint_only="constraint only",

    retrieval_weight=0.95,
    injection_weight=0.95,

    distance_from_entry=4
)

fact_node = Candidate(
    id="F-01",
    title="Bed Capacity",
    type="FACT",

    content_full="full",
    content_compressed="compressed",
    content_constraint_only="constraint only",

    retrieval_weight=0.40,
    injection_weight=0.20,

    distance_from_entry=4
)

decision_node = Candidate(
    id="D-01",
    title="Paracetamol First",
    type="DECISION",

    content_full="full",
    content_compressed="compressed",
    content_constraint_only="constraint only",

    retrieval_weight=0.80,
    injection_weight=0.85,

    distance_from_entry=2
)

print(assign_compression_level(constraint_node))
print()
print(assign_compression_level(fact_node))
print()
print(assign_compression_level(decision_node))