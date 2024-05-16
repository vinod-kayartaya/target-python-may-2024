def main():
    nums = [10, 20, 30, 40, 11, 13, 16, 17, 15, 891, 29]
    print(nums[5])  # 6th element --> 13
    # print(nums[1000]) # IndexError
    print(nums[-1])  # last element
    n = 888
    if n in nums:
        idx = nums.index(n)
        print(idx)

    print(nums[3:7])  # from index 3 to index 6
    print(nums[3:])  # from index 3 
    print(nums[:7])  # upto index 6

    print(nums[3:7:1])  # from index 3 to index 6
    print(nums[::2])  
    print(nums[1::2]) 

    print(nums[::-1])



if __name__ == '__main__':
    main()

