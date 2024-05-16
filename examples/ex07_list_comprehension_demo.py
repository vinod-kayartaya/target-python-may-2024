def main():
    nums = [10, 20, 30, 40, 11, 13, 16, 17, 15, 891, 29]

    # even_nums = []
    # for each_num in nums:
    #     if each_num % 2 == 0:
    #         even_nums.append(each_num)

    even_nums = [n for n in nums if n%2==0]
    odd_nums = [n for n in nums if n%2]

    print(nums)
    print(even_nums)
    print(odd_nums)

    names = ["vinod", "SHYAM", "John", 123, False, "Jane", "MILLER", "Robert"]
    # codes = []
    # for name in names:
    #     codes.append(name[:3].upper())

    codes = [n[:3].upper() for n in names if type(n) == str]
    rev_names = [n[::-1] if type(n) == str else n for n in names ]
    
    print(names)
    print(codes)
    print(rev_names)


if __name__ == '__main__':
    main()

