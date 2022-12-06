nums = [int(i) for i in input()]
if len({nums[i] - nums[i+1] for i in range(len(nums)-1)}) > 1:
    print('흥칫뿡!! <(￣ ﹌ ￣)>')
else:
    print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')