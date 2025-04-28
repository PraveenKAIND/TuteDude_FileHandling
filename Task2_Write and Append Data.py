y = input("Enter your name: \n ")

file2 = open('Output.txt','r+')
#mode= r,w,a,r+
writing_file=file2.write(y)
print(writing_file)
file2.close()


file2 = open ('Output.txt','a')
append_file = file2.write('\t I am a studnet of python')
print(append_file)
file2.close()

