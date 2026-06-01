import tiktoken

# Claude-compatible tokenizer
_encoder = tiktoken.get_encoding("cl100k_base")


def count_tokens(text: str) -> int:
    """
    Count tokens using cl100k_base encoding.
    """
    return len(_encoder.encode(text))


def count_three_sources(
    system_prompt: str,
    context_string: str,
    user_message_estimate: int = 200
) -> dict:
    """
    Count ALL THREE sources:
    1. System Prompt
    2. Context String
    3. User Message Reserve
    """

    system_tokens = count_tokens(system_prompt)
    context_tokens = count_tokens(context_string)

    total = (
        system_tokens
        + context_tokens
        + user_message_estimate
    )

    budget = 4000

    return {
        "system_prompt_tokens": system_tokens,
        "context_tokens": context_tokens,
        "user_message_tokens": user_message_estimate,
        "total_tokens": total,
        "budget": budget,
        "remaining_tokens": budget - total,
        "over_budget": total > budget
    }