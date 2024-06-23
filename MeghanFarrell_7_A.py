def main():
    sentences = []  # List to store the sentences
    print("Enter sentences one by one. Type 'END' to finish.")

    while True:
        sentence = input("Enter a sentence: ")
        # Using lookahead-like check: if the sentence is "END", break the loop
        if sentence == "END":
            break
        sentences.append(sentence)

    # Display the sentences
    print("\nYou entered the following sentences:")
    for sentence in sentences:
        print(sentence)

    # Display the count of sentences
    print(f"\nTotal number of sentences: {len(sentences)}")


if __name__ == "__main__":
    main()