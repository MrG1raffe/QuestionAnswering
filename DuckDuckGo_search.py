from langchain.tools import DuckDuckGoSearchRun

def duckduckgo_search(
    question: str, 
    max_results: int = 5
) -> str :
    search = DuckDuckGoSearchRun(max_results=max_results)
    return '- ' + '\n-'.join(search.run(question).split('...')[:-1])
