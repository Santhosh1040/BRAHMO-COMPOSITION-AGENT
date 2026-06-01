from data_loader import load_candidates

candidates = load_candidates()

print(f"Loaded {len(candidates)} candidates")

print("\nFirst Candidate:\n")

print(candidates[0])