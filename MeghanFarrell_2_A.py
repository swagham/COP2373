#List of common spam keywords.
spam_keywords = [
    "Job Listing", "Congratulations", "Click here", "Act now", "Urgent",
    "Limited time", "Winner", "Exclusive deal", "Risk-free", "100%",
    "No obligation", "Credit card", "Earn money", "Extra savings", "Cash bonus",
    "Investment", "Opportunity", "Lowest price", "Miracle", "Gift",
    "Guarantee", "No cost", "Offer expires", "Call now", "Order now",
    "Deal", "Cheap", "Save big", "Limited offer", "Profit"
]

def calculate_spam_score(message):
    spam_score = 0
    found_keywords = []

    #Check each keyword in the spam_keywords list.
    for keyword in spam_keywords:
        #If the keyword is found in the message, increase the spam score by 1.
        if keyword.lower() in message.lower():
            spam_score += 1
            found_keywords.append(keyword)

    return spam_score, found_keywords

def get_spam_likelihood(score):
    if score == 0:
        return "Not Spam"
    elif 1 <= score <= 5:
        return "Low Likelihood of Spam"
    elif 6 <= score <= 15:
        return "Moderate Likelihood of Spam"
    else:
        return "High Likelihood of Spam"

def main():
    #Prompt the user to enter an email message.
    email_message = input("Enter your email message: ")
    #Calculate the spam score and found messages.
    spam_score, found_keywords = calculate_spam_score(email_message)
    #Determine the likelihood of the message being spam.
    spam_likelihood = get_spam_likelihood(spam_score)

    #Display the Spam Analysis Report.
    print("\nSpam Analysis Report")
    print("====================")
    print(f"Spam Score: {spam_score}")
    print(f"Likelihood of Spam: {spam_likelihood}")
    if found_keywords:
        print(f"Keywords Found: {', '.join(found_keywords)}")

if __name__ == "__main__":
    #Entry point of the script.
    main()