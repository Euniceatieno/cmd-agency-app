# BRIEF
# You’ll play the role of a programmer who has been hired by a real estate agent to help determine what
#  a fair market price for rent should be across a number of owned properties. The good news is that the
#   real estate developer has gathered data into a spreadsheet (in a CSV file). The bad news is that the 
#   spreadsheet is so large that they can’t even open it in a typical spreadsheet program, let alone do any
#    sort of analysis with it. They’ve asked you to develop an interactive program that will perform some
#     basic exploration of the data. You’ll use Python to tackle this challenge, and gain valuable experience 
#     processing CSV files and sorting lists as well as working with files, strings, and command-line arguments.

# Checkpoint 1: Sorting Algorithms

# The real estate developer you’re working with wants a program that can non-interactively read,
#  sort, and write out the sorted data to a new file. You’ll create this new program using the CSV, 
#  ABC, and time libraries. But instead of relying on Python’s built-in lists, you’ll implement the 
#  program with your own custom lists and sorting routines—gaining hands-on experience working with 
#  commonly used data structures and algorithms, demystifying all the work Python does for us.
import csv


class SortData:
    def  __init__(self,):
        pass

    def sortData():

        

        rank = 0
        with open('data.csv', 'r') as file:
            csv_reader = csv.reader(file)
            csv_list.extend(list(csv_reader))
        
        file1 = open('sorted_data.csv','w+')

        rows = csv_list[0]
        file1.write("Rank,")
        for i in rows:
            if i == rows[-1]:
                file1.write(i)
            else:
                file1.write(i + ',')
        file1.write('\n')

        csv_list = csv_list[1:]
        csv_list.sort(key= lambda x: x[-2], reverse=True)

        for i in csv_list:
            if rank == 0:
                prev_i = csv_list[csv_list.index(i)]    
                rank += 1
            else:
                prev_i = csv_list[csv_list.index(i) - 1] 
            if prev_i[-2] == i[-2]:           
                rank = rank
            else:
                rank += 1                     
            file1.write(f'{rank},')           
            for j in i:                       
                if j == i[-1] :
                    file1.write(j)
                else:
                    file1.write(j + ',')
            file1.write('\n')

        file.close()
        file1.close()



sorted=SortData()
