# importing the module
import wikipedia
 
def cut_article(content: str):
    """
    Removes useless information from the article's content. Namely, takes the part of article before 'See also' and 'References' sections.
    """
    stop_words = ["== References ==", "== See also =="]
    res = content
    for stop_word in stop_words:
        res = res.split(stop_word)[0]
    return res

def wiki_search(
    question: str, 
    max_results: int = 1
) -> str :
    # getting suggestions
    titles = wikipedia.search(question, results = max_results) # parameter to tune
    context = ""
    for title in titles:
        page_object = wikipedia.page(title)
        context = context + cut_article(page_object.content) + '\n\n'
    return context