from models.block import Block


def get_candidate_content(candidate):
    """
    Return content based on
    current compression level.
    """

    if candidate.compression_level == "FULL":
        return candidate.content_full

    elif candidate.compression_level == "COMPRESSED":
        return candidate.content_compressed

    elif candidate.compression_level == "CONSTRAINT_ONLY":
        return candidate.content_constraint_only

    return ""


def build_context(blocks: list[Block]) -> str:
    """
    Convert blocks into final context string.
    """

    sections = []

    # ==========================================
    # BLOCK 1 — ROLE FRAME
    # ==========================================

    sections.append("=== ROLE FRAME ===")
    sections.append(
        "You are assisting Dr. Vikram, "
        "Head of Orthopaedics at Supra Multi-Specialty Hospital."
    )
    sections.append("")

    # ==========================================
    # BLOCKS 2–7
    # ==========================================

    for block in blocks:

        # Skip role frame and session boundaries
        if block.id in [1, 8]:
            continue

        has_visible_candidates = any(
            c.compression_level != "OMIT"
            for c in block.candidates
        )

        if not has_visible_candidates:
            continue

        sections.append(
            f"=== {block.name.upper()} ==="
        )

        for candidate in block.candidates:

            if candidate.compression_level == "OMIT":
                continue

            content = get_candidate_content(
                candidate
            )

            sections.append(
                f"- {candidate.title}: "
                f"{content}"
            )

        sections.append("")

    # ==========================================
    # BLOCK 8 — SESSION BOUNDARIES
    # ==========================================

    sections.append("=== SESSION BOUNDARIES ===")
    sections.append(
        "Capture important decisions, "
        "constraints, protocols, and learnings "
        "from this session for future reference."
    )
    sections.append("")

    return "\n".join(sections)