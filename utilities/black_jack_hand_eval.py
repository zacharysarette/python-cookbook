import sys

def convert_face(face):
    return ['10' if i is "K" or i is "Q" or i is "J" else i for i in face]

def sum_non_a(list):
    sum = 0
    for n in list:
        if n.isdigit():
            sum += int(n)
    return sum

def max_a(a_sum, non_a_sum):
    if non_a_sum + a_sum > 21:
        return 0
    if a_sum > 0 and non_a_sum + a_sum + 10 < 21:
        return non_a_sum + a_sum + 10
    if non_a_sum + a_sum <= 21:
        return non_a_sum + a_sum
    return 0

def blackjack_hand_eval(hand_1, hand_2):
	h1 = convert_face(hand_1)
	h2 = convert_face(hand_2)
    
	a1 = h1.count("A")
	a2 = h2.count("A")

	h1SumSub = sum_non_a(h1)
	h2SumSub = sum_non_a(h2)
	
	h1Sum = max_a(a1, h1SumSub)
	h2Sum = max_a(a2, h2SumSub)

	return h1Sum > h2Sum

hand1 = sys.argv[1]
hand2 = sys.argv[2]

sys.stdout( blackjack_hand_eval(hand1, hand2))