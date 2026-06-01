from backend.composition.token_counter import count_three_sources

system_prompt = """
You are BRAHMO.
You are an organizationally aware assistant.
"""

context = """
Patient Rajan takes Warfarin.
No NSAIDs allowed.
Paracetamol recommended.
"""

result = count_three_sources(
    system_prompt=system_prompt,
    context_string=context
)

print(result)