from models.candidate import Candidate
from composition.importance_scorer import (
    calculate_priority,
    is_protected
)

constraint_node = Candidate(
    id="C-06",
    title="Warfarin Rule",
    type="CONSTRAINT",

    content_full="Full",
    content_compressed="Compressed",
    content_constraint_only="Constraint Only",

    retrieval_weight=0.99,
    injection_weight=0.95,

    distance_from_entry=4
)

fact_node = Candidate(
    id="F-01",
    title="Bed Capacity",
    type="FACT",

    content_full="Full",
    content_compressed="Compressed",
    content_constraint_only="Constraint Only",

    retrieval_weight=0.30,
    injection_weight=0.20,

    distance_from_entry=4
)

print(
    "Constraint Priority:",
    round(calculate_priority(constraint_node), 3)
)

print(
    "Fact Priority:",
    round(calculate_priority(fact_node), 3)
)

print(
    "Constraint Protected:",
    is_protected(constraint_node)
)

print(
    "Fact Protected:",
    is_protected(fact_node)
)