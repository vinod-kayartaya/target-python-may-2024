def main():
    nums = [10, 20, 30, 40, 11, 13, 16, 17, 15, 891, 29]
    print(f'there are {len(nums)} numbers in `nums`')
    my_name = 'vinod kumar k'
    print(f'there are {len(my_name)} chars in `my_name`')
    print(nums)
    nums.append(100)
    print(nums)
    nums.insert(0, 999)  # here self -> nums, index -> 0, object -> 999
    print(nums)
    list.insert(nums, 0, 888)  # here self -> nums, index -> 0, object -> 888
    print(nums)
    p = nums.pop()  # 100
    print(f'popped value is {p}')
    p = nums.pop(6)  # 11
    print(f'popped value is {p}')
    nums.remove(16)
    print(f'after removing 16, nums is {nums}')

    nums.extend(['vinod', True, 0.12])
    nums += [99, 88, 77]
    print(nums)



if __name__ == '__main__':
    main()

