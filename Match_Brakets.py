def match_brackets(str):
    s = []
    for c in str:
        if c == '{' or c == '(' or c == '[':
            s.append(c)
        elif c == '}' or c == ')' or c == ']':
            if not s:
                return False
            elif c == '}' and s[-1] == '{':
                s.pop()
            elif c == ']' and s[-1] == '[':
                s.pop()
            elif c == ')' and s[-1] == '(':
                s.pop()
        else:
            return False

    return len(s) == 0

user_input = input("Enter input: ")

print("Brackets are perfectly matched" if match_brackets(user_input) else "Brackets are NOT matched")
