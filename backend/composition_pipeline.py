from data_loader import load_candidates

from composition.compressor import (
    assign_compression_level
)

from composition.budget_fitter import (
    fit_to_budget
)

from composition.block_assembler import (
    assemble_blocks
)

from composition.context_builder import (
    build_context
)

from models.composition_result import (
    CompositionResult
)


SYSTEM_PROMPT_RESERVE = 800
USER_MESSAGE_RESERVE = 200


def run_composition(token_budget=1200):

    candidates = load_candidates()

    # Assign compression levels
    for candidate in candidates:
        assign_compression_level(candidate)

    # Total candidate tokens before compression
    current_tokens = sum(
        c.tokens_full
        for c in candidates
    )

    # Assessment requirement:
    # Reserve tokens for system prompt + user message
    available_context_budget = (
        token_budget
        - SYSTEM_PROMPT_RESERVE
        - USER_MESSAGE_RESERVE
    )

    # Budget fitting
    budget_result = fit_to_budget(
        candidates,
        current_tokens,
        available_context_budget
    )

    # Assemble blocks
    blocks = assemble_blocks(
        candidates
    )

    # Build final context
    context = build_context(
        blocks
    )

    included = len([
        c for c in candidates
        if c.compression_level != "OMIT"
    ])

    omitted = len([
        c for c in candidates
        if c.compression_level == "OMIT"
    ])

    return CompositionResult(
    blocks=blocks,
    total_tokens=budget_result["tokens"],
    nodes_included=included,
    nodes_omitted=omitted,
    compression_passes=budget_result["passes"],
    compression_log=budget_result["log"],
    context_string=context
)