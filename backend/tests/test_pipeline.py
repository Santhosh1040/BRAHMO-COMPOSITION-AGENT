from composition_pipeline import (
    run_composition
)

result = run_composition()

print("TOKENS:")
print(result.total_tokens)

print("\nINCLUDED:")
print(result.nodes_included)

print("\nOMITTED:")
print(result.nodes_omitted)

print("\nPASSES:")
print(result.compression_passes)

print("\nCONTEXT:\n")

print(result.context_string)