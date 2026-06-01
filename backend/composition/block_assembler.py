from models.block import Block
from models.candidate import Candidate


def create_default_blocks():

    return {
        1: Block(1, "Role Frame"),
        2: Block(2, "Global Constraints"),
        3: Block(3, "Recent Decisions"),
        4: Block(4, "Active Constraints"),
        5: Block(5, "Session Context"),
        6: Block(6, "Open Questions"),
        7: Block(7, "Stale Flags"),
        8: Block(8, "Session Boundaries"),
    }


def assign_candidate_to_block(
    candidate: Candidate,
    blocks: dict
):
    """
    Assign candidate to correct block.
    """

    # Stale content
    if getattr(candidate, "status", None) == "REVIEW_REQUIRED":
        block_id = 7

    # Global constraints
    elif (
        candidate.type == "CONSTRAINT"
        and candidate.zone == 2
    ):
        block_id = 2

    # Active constraints
    elif (
        candidate.type == "CONSTRAINT"
        and candidate.zone == 1
    ):
        block_id = 4

    # Decisions
    elif candidate.type == "DECISION":
        block_id = 3

    # Facts
    elif candidate.type == "FACT":
        block_id = 5

    # Anti-patterns
    elif candidate.type == "ANTI_PATTERN":
        block_id = 5

    # Questions
    elif candidate.type == "QUESTION":
        block_id = 6

    else:
        block_id = 5

    candidate.block_assignment = block_id

    blocks[block_id].candidates.append(candidate)


def assemble_blocks(
    candidates: list[Candidate]
):
    """
    Assemble all candidates into
    the 8-block context structure.
    """

    blocks = create_default_blocks()

    for candidate in candidates:

        assign_candidate_to_block(
            candidate,
            blocks
        )
def assemble_blocks(
    candidates: list[Candidate]
):
    """
    Assemble all candidates into
    the 8-block context structure.
    """

    blocks = create_default_blocks()

    for candidate in candidates:

        assign_candidate_to_block(
            candidate,
            blocks
        )

    # Calculate token counts per block
    for block in blocks.values():

        total = 0

        for candidate in block.candidates:

            if candidate.compression_level == "FULL":
                total += candidate.tokens_full

            elif candidate.compression_level == "COMPRESSED":
                total += candidate.tokens_compressed

            elif candidate.compression_level == "CONSTRAINT_ONLY":
                total += candidate.tokens_constraint_only

        block.token_count = total

    return list(blocks.values())
  