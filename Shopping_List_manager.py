file_read = open('My-Shopping_list.txt', 'r')
print("File in Read Mode")
print(file_read.read())
file_read.close()

file_append = open('My-Shopping_list.txt', 'a')
file_append.write("\n File in Append Mode ....")
file_append.write("Hi! This is my Shopping list.")
file_append.close()

file_write = open('My-Shopping_list.txt', 'w')
file_write.write("File in Write Mode ....")
file_write.write("Hi! This is my Shopping list.")
file_write.close()