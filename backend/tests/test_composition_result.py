from models.block import Block
from models.composition_result import CompositionResult

block = Block(
    id=2,
    name="Global Constraints"
)

result = CompositionResult(
    blocks=[block],
    total_tokens=2960,
    nodes_included=22,
    nodes_omitted=6,
    compression_passes=3
)

print(result)