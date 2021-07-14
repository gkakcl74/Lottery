from random import randint


def generate_numbers(n):
    numbers = []   #기본적인 랜덤 번호이다.

    while len(numbers) < n: #n은 내가 정한 번호 길이이므로 그 길이만큼 반복하라는 것이다.
        new_number = randint(1, 45)
        if new_number not in numbers: # 만약 배열 안에 같은 숫자가 없다면 넣으라는것이다.
            numbers.append(new_number)

    return numbers # 완성된 배열 numbers를 리턴한다.


def draw_winning_numbers():
    winning_numbers = generate_numbers(7) #winning_numbers 는 정답 로또 번호이다.

    return sorted(winning_numbers[:6]) + winning_numbers[6:] #0번 부터 5번까지의 배열과 6번배열 을 붙여 리턴한다.


def count_matching_numbers(numbers, winning_numbers):
    count = 0

    for num in numbers:
        if num in winning_numbers: # numbers의 한 값을 나타내는 num이 winning_numbers에 겹친다면 count += 1 을 한다.
            count = count + 1

    return count #누적된 count를 리턴시킨다.


def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])  #numbers 배열과 winning... 의 겹친 횟수를 count에
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:]) #마지막 보너스번호가 numbers에서 겹친횟수를 bonus... 에

    #겹친횟수만큼 리턴한다.
    if count == 6:
        return 1000000000
    elif count == 5 and bonus_count == 1: #bonus_count 즉 마지막 번호 보너스 번호가 겹치면 count가 1 인것이다.
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0

