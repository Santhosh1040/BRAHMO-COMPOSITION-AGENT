from dataclasses import dataclass


@dataclass
class Candidate:
    id: str

    title: str

    type: str

    content_full: str
    content_compressed: str
    content_constraint_only: str

    retrieval_weight: float
    injection_weight: float

    distance_from_entry: int

    zone: int = 1

    importance: float = 0.0

    department: str | None = None

    status: str = "ACTIVE"

    tokens_full: int = 0
    tokens_compressed: int = 0
    tokens_constraint_only: int = 0

    compression_level: str = "FULL"

    block_assignment: int | None = None