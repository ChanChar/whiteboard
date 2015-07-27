def readmore(test):
    if len(test) <= 55:
        return test
    trimmed = test[:40]
    if trimmed.rfind(' ') != -1:
        trimmed = trimmed[:trimmed.rfind(' ')]
    return trimmed + '... <Read More>'

tests = [
"Tom exhibited.",
"Amy Lawrence was proud and glad, and she tried to make Tom see it in her face - but he wouldn't look.",
"Tom was tugging at a button-hole and looking sheepish.",
"Two thousand verses is a great many - very, very great many.",
"Tom's mouth watered for the apple, but he stuck to his work."
]

for test in tests:
    print(readmore(test))
