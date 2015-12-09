fileName = "translations.csv"

READ = "r"

userText = raw_input("What is the text message you would like to translate?").lower()

userWords = userText.split()

translatedWords = []

for word in userWords:
    counter = 0
    wordTranslated = False

    with open(fileName, mode=READ) as translationFile:
        for row in translationFile:
            wordsInRow = row.split(",")

            if word == wordsInRow[0].lower():
                translatedWords.append(wordsInRow[1].rstrip("\n").lower())
                wordTranslated = wordTranslated = True
                counter = counter + 1

        if wordTranslated == False and counter == 0:
            translatedWords.append(word)

print(" ".join(translatedWords))
