from models.candidate import Candidate


def assign_compression_level(candidate: Candidate):
    """
    Assign compression level based on
    distance and node type.
    """

    # Sacred rule
    if candidate.type == "CONSTRAINT":
        candidate.compression_level = "FULL"
        return candidate

    if candidate.distance_from_entry <= 1:

        candidate.compression_level = "FULL"

    elif candidate.distance_from_entry == 2:

        candidate.compression_level = "COMPRESSED"

    else:

        candidate.compression_level = "CONSTRAINT_ONLY"

    return candidate