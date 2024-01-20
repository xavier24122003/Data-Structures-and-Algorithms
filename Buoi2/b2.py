#Tran Huynh Trung Hieu
#N21DCCN122
#D21CQCN02-N

def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num
        # Kiểm tra xem complement đã xuất hiện trước đó trong mảng hay không
        if complement in seen:
            print(seen)
            # Nếu có, trả về chỉ số của complement và chỉ số hiện tại
            return [seen[complement], i]
        # Nếu không, lưu trữ giá trị và chỉ số hiện tại vào dictionary
        print(seen)
        seen[num] = i
    
    # Trường hợp không tìm thấy cặp số nào thỏa mãn
    return None

nums = [1,4,9,4,1,2,1]
target = 6
result = twoSum(nums, target)
print(result)
