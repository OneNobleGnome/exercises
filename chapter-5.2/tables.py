'''def print_2_column_header(column_header_1,column_header_2,):
    print(column_header_1,column_header_2, sep='\t')
    length_of_line = len(column_header_1)+4+len(column_header_2)
    length_of_line =  str(length_of_line * "-")
    print(length_of_line)
   ''' 
    
def print_2_column_header(column_header_1,column_header_2,):
    print(column_header_1,"    ",column_header_2,)
    length_of_line = len(column_header_1)+4+len(column_header_2)
    length_of_line =  str(length_of_line * "-")
    print(length_of_line)
    
    
    
def print_3_column_header(column_header_1,column_header_2,column_header_3):
    print(column_header_1,column_header_2, column_header_3)
    length_of_line = len(column_header_1)+4+len(column_header_2)
    length_of_line =  str(length_of_line * "-")
    print(length_of_line)
    
