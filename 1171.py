n = int(input())
nums = []
for c in range(n):
    nums.append(int(input()))
isolados = set(nums)
for c in isolados:
    print(f"{c} aparece {nums.count(c)} vez(es)")