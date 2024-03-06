def to_rövarspråket(text):
    konsonanter = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    rövarspråket = ""

    for bokstav in text:
        if bokstav in konsonanter:
            rövarspråket += bokstav + "o" + bokstav
        else:
            rövarspråket += bokstav

    return rövarspråket


text = input("Skriv en text: ")
result = to_rövarspråket(text)
print("Rövarspråk:", result)
