from transformers import pipeline

def mdeberta_request(
    question: str,
    context: str
):
    qa_model = pipeline("question-answering", "timpal0l/mdeberta-v3-base-squad2")
    res = qa_model(question = question, context = context)
    if res['score'] > 0.5:
        return res['answer']
    else:
        return "I DO NOT KNOW"