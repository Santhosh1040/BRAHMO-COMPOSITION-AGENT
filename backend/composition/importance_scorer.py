from models.candidate import Candidate


def calculate_priority(candidate: Candidate) -> float:
    """
    Combined composition priority.

    Retrieval:
    Should the node be recalled?

    Injection:
    How much context space should it get?
    """

    return (
        candidate.retrieval_weight * 0.4
        + candidate.injection_weight * 0.6
    )


def is_protected(candidate: Candidate) -> bool:
    """
    CONSTRAINT nodes are protected.
    """

    return candidate.type == "CONSTRAINT"