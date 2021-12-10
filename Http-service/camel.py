def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)
print(solution("AlfredENeumann"))

if __name__ == '__main__':
    solution()