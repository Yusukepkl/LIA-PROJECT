def check_consistency(google_result: str, openai_result: str, grook_result: str) -> bool:
    """Verifica se há divergências entre as três respostas"""
    return google_result.strip().lower() == openai_result.strip().lower() == grook_result.strip().lower()
