fileName = "translations.csv"

READ = "r"

userText =  raw_input("What is the text message you would like to translate?").lower()

userWords = userText.split()

translatedWords = []

with open(fileName, mode=READ) as translationFile:

    # for row in translationFile:
    for word in userWords:
        for row in translationFile:
            wordsInRow = row.split(",")
            if word == wordsInRow[0].lower():
                translatedWords.append(wordsInRow[1].lower())


print(translatedWords)
