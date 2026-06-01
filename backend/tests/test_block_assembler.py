from models.candidate import Candidate
from composition.block_assembler import assemble_blocks

candidates = [

    Candidate(
        id="D-01",
        title="Recent Decision",
        type="DECISION",

        content_full="full",
        content_compressed="compressed",
        content_constraint_only="constraint",

        retrieval_weight=0.8,
        injection_weight=0.9,

        distance_from_entry=1
    ),

    Candidate(
        id="C-01",
        title="Warfarin Rule",
        type="CONSTRAINT",

        content_full="full",
        content_compressed="compressed",
        content_constraint_only="constraint",

        retrieval_weight=0.95,
        injection_weight=0.95,

        distance_from_entry=1
    ),

    Candidate(
        id="F-01",
        title="Bed Capacity",
        type="FACT",

        content_full="full",
        content_compressed="compressed",
        content_constraint_only="constraint",

        retrieval_weight=0.2,
        injection_weight=0.2,

        distance_from_entry=4
    )
]

blocks = assemble_blocks(candidates)

for block in blocks:
    if block.candidates:
        print(
            f"{block.name}: "
            f"{len(block.candidates)} node(s)"
        )