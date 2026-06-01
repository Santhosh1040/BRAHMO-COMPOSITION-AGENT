from composition.importance_scorer import (
    is_protected
)


def fit_to_budget(
    candidates,
    current_tokens,
    budget
):
    """
    Iteratively compress nodes until
    token count fits budget.
    """

    compression_log = []

    passes = 0

    while current_tokens > budget:

        # Only non-protected and non-omitted nodes
        compressible = [
            c for c in candidates
            if not is_protected(c)
            and c.compression_level != "OMIT"
        ]

        if not compressible:
            break

        # Assessment rule:
        # lowest injection_weight first
        compressible.sort(
            key=lambda x: x.injection_weight
        )

        node = compressible[0]

        old_level = node.compression_level

        if node.compression_level == "FULL":

            saved = (
                node.tokens_full
                - node.tokens_compressed
            )

            node.compression_level = "COMPRESSED"

        elif node.compression_level == "COMPRESSED":

            saved = (
                node.tokens_compressed
                - node.tokens_constraint_only
            )

            node.compression_level = "CONSTRAINT_ONLY"

        elif node.compression_level == "CONSTRAINT_ONLY":

            saved = node.tokens_constraint_only

            node.compression_level = "OMIT"

        else:
            continue

        current_tokens -= max(saved, 0)

        passes += 1

        compression_log.append(
            f"Pass {passes}: "
            f"{node.title} "
            f"{old_level} -> "
            f"{node.compression_level} "
            f"(saved {saved})"
        )

    return {
        "tokens": current_tokens,
        "passes": passes,
        "log": compression_log
    }