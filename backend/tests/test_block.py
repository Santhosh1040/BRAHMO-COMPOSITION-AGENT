from models.candidate import Candidate
from models.block import Block

candidate = Candidate(
    id="C-01",
    title="Warfarin-NSAID Interaction",
    content="No NSAIDs with Warfarin",
    block_type="GLOBAL_CONSTRAINTS",
    retrieval_weight=0.98,
    injection_weight=0.95
)

block = Block(
    id=2,
    name="Global Constraints"
)

block.candidates.append(candidate)

print(block)