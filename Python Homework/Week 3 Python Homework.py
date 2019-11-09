#A program that counts for the user; asks them where to starts, end, and what to count by

start = int(input("Start at: "))
end = int(input("End at: "))
count_by = int(input("Count by: "))

while start <= end:
    print(start)
    start += count_by
