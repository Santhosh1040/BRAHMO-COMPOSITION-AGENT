from dataclasses import dataclass, field
from typing import List
from models.candidate import Candidate


@dataclass
class Block:
    id: int
    name: str
    candidates: List[Candidate] = field(default_factory=list)
    token_count: int = 0