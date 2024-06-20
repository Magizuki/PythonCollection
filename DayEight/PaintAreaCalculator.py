import math

def paint_calc(height, width, cover):
    result = int(math.ceil(float(height * width) / float(cover)))
    print(f"you'll need {result} cans of paint.")

test_h = int(input())
test_w = int(input())
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)