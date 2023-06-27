#! python3
# Table Printer Practice Project




tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

# COLUMNS: 3 and right-justified
# ROWS: 4

#  first have to find the longest string in each of the
#  inner lists so that the whole column can be wide enough to fit all the strings  


def printTable(tableData):

    # Find the maximum length of each string in each inner list
    colWidths = [max(len(str(item)) for item in col) for col in tableData]

    # Determine the number of rows and columns in the table
    numRows = len(tableData[0])
    numCol = len(tableData)

    # Print the table, right-justified
    for i in range(numRows):
        for j in range(numCol):
            print(str(tableData[j][i]).rjust(colWidths[j]), end=' ')
        print()
       

printTable(tableData)