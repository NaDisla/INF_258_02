new_file = open('numbers.txt', 'a')
new_file.write("\nOtra cosa diferente")
for i in range(1,10):
    new_file.write(f"{str(i)}\n")
new_file.close()

read_file = open('numbers.txt', 'r')
file_content = read_file.readlines()
for r in file_content:
    print(r)
read_file.close()

read_file = open('test.csv', 'r')
file_content = read_file.readlines()
file_split = file_content[0].split(',')

file_dict = {}
list_dict = []
for name in file_split:
    list_dict.append({'Nombre': name})
print(list_dict)
list_dict[0]['Nombre'] = 'Pedro'
print(list_dict[0])
read_file.close()