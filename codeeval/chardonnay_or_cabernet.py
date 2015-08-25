from collections import Counter
def find_wines(wines, search_letters):
    search_params = Counter(search_letters)
    matched_wines = []
    for wine in wines:
        wine_letters = Counter(wine.lower())
        if all([search_params[letter] <= wine_letters[letter] for letter in search_params]):
            matched_wines.append(wine)

    if len(matched_wines) == 0:
        return False

    return " ".join(matched_wines)

# Example
test = "Chardonnay Sauvignon | ann\n"
wines, letters = test.strip().split(' | ')
wines = wines.split()
print(find_wines(wines, letters))
