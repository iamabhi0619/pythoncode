numbers = range(5)
print(numbers)

marks =[95, 98, 97, "Maths", "Physics", "Chemistry"]
print(marks[0], marks[3])

print(marks[-1], marks[-4])#index can be negative
print(marks[5], marks[2])#- index backward counting
print(marks[0:3])#range of array

marks.append("Biology")
print(marks)

marks.insert(3, 99)
print(marks)

print(87 in marks)

print(len(marks))

i=0
while i < len(marks):
    print(marks[i])
    i = i+1

for marks in marks:
    if marks == "Maths":
        break;
    print(marks)
