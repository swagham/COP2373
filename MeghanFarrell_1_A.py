def sell_tickets():
    """Function to handle the pre-sale of cinema tickets."""
    total_tickets = 20  # Total tickets available for sale
    total_buyers = 0  # Accumulator for the total number of buyers

    while total_tickets > 0:
        print(f"\nThere are {total_tickets} tickets remaining.")
        try:
            # Prompt the user for the number of tickets they want to buy
            num_tickets = int(input("How many tickets would you like to buy (1-4)? "))

            if 1 <= num_tickets <= 4:
                if num_tickets <= total_tickets:
                    # Update the number of remaining tickets and increment the buyer count
                    total_tickets -= num_tickets
                    total_buyers += 1
                    print(f"Thank you for your purchase! You bought {num_tickets} tickets.")
                else:
                    # Inform the user if the requested number of tickets exceeds the remaining tickets
                    print(f"Sorry, we only have {total_tickets} ticket(s) left.")
            else:
                # Inform the user if the input is out of the valid range
                print("You can only buy between 1 and 4 tickets.")
        except ValueError:
            # Handle invalid input gracefully
            print("Invalid input. Please enter a number between 1 and 4.")

    # Display the final results when all tickets are sold
    print("\nAll tickets have been sold.")
    print(f"Total number of buyers: {total_buyers}")


if __name__ == "__main__":
    sell_tickets()