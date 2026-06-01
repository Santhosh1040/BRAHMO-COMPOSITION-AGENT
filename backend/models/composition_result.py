from dataclasses import dataclass, field
from typing import List

from models.block import Block


@dataclass
class CompositionResult:
    blocks: List[Block] = field(default_factory=list)

    total_tokens: int = 0
    nodes_included: int = 0
    nodes_omitted: int = 0

    compression_passes: int = 0

    compression_log: List[str] = field(
        default_factory=list
    )

    context_string: str = ""