class MatingGame:
    def __init__(self, your_name, partner_name):
        self.your_name = your_name.replace(" ", "").lower()
        self.partner_name = partner_name.replace(" ", "").lower()

    def calculate_remaining_characters(self):
        your_name_chars = list(self.your_name)
        partner_name_chars = list(self.partner_name)

        for char in your_name_chars[:]:
            if char in partner_name_chars:
                your_name_chars.remove(char)
                partner_name_chars.remove(char)

        return "".join(your_name_chars), "".join(partner_name_chars)

    def calculate_relationship(self):
        your_remaining, partner_remaining = self.calculate_remaining_characters()
        your_count = len(your_remaining)
        partner_count = len(partner_remaining)
        total_sum = your_count + partner_count

        if total_sum == 0:
            return (
                your_remaining,
                partner_remaining,
                your_count,
                partner_count,
                total_sum,
                "Not Compatible! </3",
            )

        flames = ["F", "L", "A", "M", "E", "S"]
        while len(flames) > 1:
            idx = (total_sum % len(flames)) - 1
            if idx >= 0:
                flames = flames[idx + 1:] + flames[:idx]
            else:
                flames.pop()

        flames_result = {
            "F": "Friendship",
            "L": "Friendship",
            "A": "Friendship",
            "M": "Marriage",
            "E": "Friendship",
            "S": "Not Compatible! </3",
        }
        return (
            your_remaining,
            partner_remaining,
            your_count,
            partner_count,
            total_sum,
            flames_result[flames[0]],
        )


while True:
    your_name = input("\nYour name: ")
    partner_name = input("Crush name: ")

    game = MatingGame(your_name, partner_name)
    (
        your_remaining,
        partner_remaining,
        your_count,
        partner_count,
        total_sum,
        relationship,
    ) = game.calculate_relationship()

    print("\n----------------------------------------")
    print(f"\nYour name remaining: {your_remaining}")
    print(f"Crush name remaining: {partner_remaining}")
    print(f"Count remaining [your name]: {your_count}")
    print(f"Count remaining [crush]: {partner_count}")
    print(f"Sum: {total_sum}")
    print(f"Relationship: {relationship}")
    print("\n----------------------------------------")


    try_again = input("\nWould you like to try again? (yes/no): ").strip().lower()
    if try_again != "yes":
        print("Exiting the program. Goodbye!")
        break