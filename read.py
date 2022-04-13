data = []
count = 0

with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))

sum_len = 0
for d in data:        
        sum_len += len(d) 
        
print('檔案讀取完畢，總共有', len(data), '筆資料')
print('留言平均長度為', sum_len / len(data))
#sum, average

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
    
print(new[0])
#filtering

good = [d for d in data if 'good' in d]
print('一共有', len(good), '筆留言提到good')

bad = ['bad' in d for d in data]
print(bad)
#list comprehension快寫法篩選



