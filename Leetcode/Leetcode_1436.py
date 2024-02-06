def destCity(paths) -> str:
    start_cities = set()
    end_cities = set()
    for path in paths:
        start_cities.add(path[0])
        end_cities.add(path[1])
    return (end_cities-start_cities).pop()


def solution2(paths) -> str:
        start_cities, end_cities = map(set, zip(*paths))
        destination = (end_cities - start_cities).pop()
        return destination

paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(solution2(paths))