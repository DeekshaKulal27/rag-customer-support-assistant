def format_prompt(context, query, intent):
    return f"""
You are a professional customer support assistant.

Intent: {intent}

Use the context below to answer politely.

Context:
{context}

Question:
{query}

Answer:
"""