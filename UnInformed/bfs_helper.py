# Shyamal Vaderia : 2015A7PS0048P

def solution(root):
    seq = list()
    while root.parent != None:
        seq.append(root.action)
        root = root.parent
    return seq

def main():
    pass

if __name__ == "__main__":
    main()
