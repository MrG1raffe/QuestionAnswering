from openai import OpenAI


def chat_gpt_request(
    key: str,
    question: str,
    context: str = None
):
    client = OpenAI(api_key=key)

    if context is not None:
        request = f"""
        Give concise answers without justifying and without making sentences, with the context that I give you. \n
        Context: {context} \n
        Question: {question}
        """
    else:
        request = f"""
        Give concise answers without justifying and without making sentences. \n
        Question: {question}
        """

    result = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": request,
            }
        ],
        model="gpt-3.5-turbo",
    )

    return result.choices[0].message.content
