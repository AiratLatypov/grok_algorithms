from collections import deque

# пример реализации графа на python
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def person_is_seller(name: str):
    # можно заменить на необходимую нам логику
    return name[-1] == "m"
    # return len(name) == 6


def search(name: str):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if not person in searched: # проверяем, чтобы не получить бесконечный цикл
            if person_is_seller(person):
                print(person, "is a mango seller")
                return True

            else:
                search_queue += graph[person]
    return False

search("you")
