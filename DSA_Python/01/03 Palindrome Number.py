def palindrome_check_string(word):
    word = str(word)
    left = 0
    right = len(word)-1
    while (left <= right):
        if word[left]!=word[right]:
            return False
        else:
            left = left +1
            right = right -1
    return True

tocheck='malayalam'
print(palindrome_check_string(tocheck))


def palindrome_num_check(num):
    num = str(num)
    if (num==num[::-1]):
        return True
    else:
        return False
    
num = 101
print(palindrome_num_check(num))