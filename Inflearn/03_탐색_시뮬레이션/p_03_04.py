'''
4. 두 리스트 합치기
오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로그램
'''

_ = input()
nums = input() + " "
_ = input()
nums += input()
nums = list(map(int, nums.split()))
print(" ".join(map(str,sorted(nums))))

