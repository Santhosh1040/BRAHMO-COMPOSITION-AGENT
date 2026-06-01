from database import get_candidate_nodes
from models.candidate import Candidate


def load_candidates():
    rows = get_candidate_nodes()

    candidates = []

    for row in rows:

        candidate = Candidate(
            id=row["id"],
            title=row["title"],
            type=row["type"],

            content_full=row["content_full"],
            content_compressed=row["content_compressed"],
            content_constraint_only=row["content_constraint_only"],

            retrieval_weight=float(row["retrieval_weight"]),
            injection_weight=float(row["injection_weight"]),

            distance_from_entry=row["distance_from_entry"],
            zone=row["zone"],

            importance=float(row["importance"]),

            department=row["department"],

            status=row["status"],

            tokens_full=row["tokens_full"],
            tokens_compressed=row["tokens_compressed"],
            tokens_constraint_only=row["tokens_constraint_only"]
        )

        candidates.append(candidate)

    return candidates