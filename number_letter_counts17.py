# Number letter counts Q17

#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
# how many letters would be used?


# based on https://euler.beerbaronbill.com/en/latest/solutions/17.html
def number_to_english(n: int):
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
            "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = [None, None, "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if 0 <= n < 20:
        return ones[n]
    elif 20 <= n <= 90 and n % 10 == 0:
        return tens[n // 10]
    elif 20 < n < 100:
        return tens[n // 10] + "-" + ones[n % 10]
    elif 100 <= n <= 900 and n % 100 == 0:
        return ones[n // 100] + " hundred"
    elif 100 < n < 1000:
        return ones[n // 100] + " hundred and " + number_to_english(n % 100)
    elif 1000 < n < 10000:
        pass
    elif n == 1000:
        return "one thousand"
    else:
        raise ValueError("unexpected input")



iterations = 1000
answer = 0
for i in range(iterations):
    words = number_to_english(i + 1).replace(" ", "").replace("-", "")
    answer += len(words)

print(answer) #21124

