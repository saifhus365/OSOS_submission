import tiktoken


def chunk_text(text, max_tokens=300, overlap=50):
    """
    Splits a large text into chunks using cl100k_base tokenizer.

    Args:
        text (str): The full text to split.
        max_tokens (int): Max number of tokens per chunk.
        overlap (int): Number of tokens to overlap between chunks.

    Returns:
        List of chunk strings.
    """
    tokenizer = tiktoken.get_encoding("cl100k_base")
    tokens = tokenizer.encode(text)

    chunks = []
    start = 0

    while start < len(tokens):
        end = min(start + max_tokens, len(tokens))
        chunk = tokenizer.decode(tokens[start:end])
        chunks.append(chunk)
        start += max_tokens - overlap

    return chunks
