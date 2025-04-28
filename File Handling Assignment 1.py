#1 Method
try:
    file2 = open('sample1.txt','r+')
    #mode= r,w,a,r+
    writing_file=file2.write(' This is a Sample Text File \n It contains multiple lines')
    print(writing_file)
    file2.close()

    file2 = open('sample.1txt','r+')
    #mode= r,w,a,r+
    reading_file=file2.read()
    print(reading_file)
    file2.close()

except FileNotFoundError:
    print('Sorry File not found')

else:
    print("Pass")