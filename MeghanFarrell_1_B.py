import random


def create_responses_file():
    """Create a file with Magic 8 Ball responses."""
    # List of predefined Magic 8 Ball responses
    responses = [
        "Yes, of course!",
        "Without a doubt, yes.",
        "You can count on it.",
        "For sure!",
        "Ask me later!",
        "I'm not sure.",
        "I can't tell you right now.",
        "I'll tell you after my nap.",
        "No way!",
        "I don't think so.",
        "Without a doubt, no.",
        "The answer is clearly NO!"
    ]

    # Write the responses to a file called '8ball_responses.txt'
    with open('8ball_responses.txt', 'w') as file:
        for response in responses:
            file.write(response + '\n')  # Write each response on a new line


def read_responses_file():
    """Read the responses from the file and return them as a list."""
    # Open the file '8ball_responses.txt' for reading
    with open('8ball_responses.txt', 'r') as file:
        responses = file.readlines()
    # Remove newline characters from each response and return the list
    return [response.strip() for response in responses]


def magic_8_ball():
    """Simulate the Magic 8 Ball."""
    # Ensure the responses file is created
    create_responses_file()
    # Load the responses from the file into a list
    responses = read_responses_file()

    while True:
        # Prompt the user to ask a yes/no question
        question = input("Ask a yes/no question (or type 'quit' to exit): ")
        if question.lower() == 'quit':
            # If the user types 'quit', exit the loop and say goodbye
            print("Goodbye!")
            break
        else:
            # Select and display a random response from the list
            print(random.choice(responses))


if __name__ == "__main__":
    magic_8_ball()