from data_loader import load_candidates

from composition.compressor import assign_compression_level
from composition.block_assembler import assemble_blocks
from composition.context_builder import build_context


candidates = load_candidates()

# Assign compression level to every candidate
for candidate in candidates:
    assign_compression_level(candidate)

blocks = assemble_blocks(candidates)

context = build_context(blocks)

print(context)