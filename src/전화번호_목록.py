
def solution(phone_book):
    phone_numbers = set(phone_book)

    for number in phone_numbers:
        for j in range(1, len(number)):
            if number[:j] in phone_numbers:
                return False
    return True
