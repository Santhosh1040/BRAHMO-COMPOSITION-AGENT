from database import get_candidate_nodes

nodes = get_candidate_nodes()

print(f"Fetched {len(nodes)} nodes")

print("\nFirst Node:\n")

print(nodes[0])