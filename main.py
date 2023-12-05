def openBook(file_path):
    with open(file_path) as f:
        return f.read()

def countWords(text):
    words = text.split()
    return len(words)

def countLetters(text):
    counter = {}
    for c in text:
        counter[c.lower()] = 1 + counter.get(c.lower(),0)
    return counter

def printLetters(charCount):
    charList = charCount.items()
    sortedList = sorted(charList,key=lambda x: x[1], reverse=True)
    for k, v in sortedList:
        if k.isalpha():
            print(f"The '{k}' character was found {v} times")

def main():
    bookPath = "/home/bb/Projects/bootdev/bookbot/books/frankenstein.txt"
    text = openBook(bookPath)
    wordCount = countWords(text)
    characterCount = countLetters(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wordCount} words found in the document.")
    print("\n")
    printLetters(characterCount)

main()

