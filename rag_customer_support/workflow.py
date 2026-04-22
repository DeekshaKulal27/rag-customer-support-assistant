def detect_intent(query):
    q = query.lower()

    if "refund" in q:
        return "refund"
    elif "shipping" in q or "delivery" in q:
        return "shipping"
    elif "cancel" in q:
        return "cancel"
    elif "exchange" in q:
        return "exchange"
    elif "legal" in q or "complaint" in q:
        return "human"
    else:
        return "general"


def escalation_needed(query, docs):
    if len(docs) == 0:
        return True
    if "lawyer" in query.lower():
        return True
    return False