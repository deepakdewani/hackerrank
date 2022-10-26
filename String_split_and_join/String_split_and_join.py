def split_and_join(line):
    # write your code here
    lines = line.split()
    line = ('-').join(lines)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)