def main():

    def read_frankenstein_book():
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
            return file_contents

    def get_number_of_words_in_frankenstein_book():
        words_in_book = len(read_frankenstein_book().split())
        return words_in_book

    def get_frankenstein_character_count():
        all_letters_count = {}
        all_letters = read_frankenstein_book().lower().replace(" ", "")

        for letter in all_letters:
            all_letters_count[letter] = 0

        for key in all_letters_count:
            all_letters_count[key] = all_letters.count(key)

        return all_letters_count

    def print_character_report():

        character_list = []
        
        print("--- Begin report of books/frankenstein.txt ---")
        print(f'{get_number_of_words_in_frankenstein_book()} words found in the document')

        for key, value in get_frankenstein_character_count().items():
            if key.isalpha():
                character_list.append({"Key": key, "Value": value})

        character_list.sort(reverse=True, key=lambda x: x["Value"])
        
        for entry in character_list:
            print(f"The '{entry["Key"]}' character was found {entry['Value']} times")
        
        # print(character_list)
        
        print("--- End report ---")

    print_character_report()


main()
