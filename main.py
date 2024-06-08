actual_data_start_from=18
scale_factor =  0.003635/8388608.000000
t_value= 0.000
increment_by = 0.004
title_first_line=[ "PGV(cm/s)","RD  4.638694226741791E-003"]
title_second_line=["t","vel.RD"]
actual_starting_line=0
destination_file_name='ST011806150000_copy.RD'
source_file_name='1806150000ST01_0004.EW'

def get_scientific_notation(number):
    if number >= 0:
        return " "+"{:.7e}".format(number * scale_factor)+" "
    return "{:.7e}".format(number * scale_factor)

def get_destination_file_content(lineContent,t_value):
    number_strings = lineContent.split()
    numbers = ["{:.3f}".format(t_value).ljust(20)] + [get_scientific_notation(int(num)).ljust(20) for num in number_strings]
    return "\t".join(numbers)
    
    
   

# Open the source file for reading
with open(f'./{source_file_name}', 'r') as source_file:
    with open(destination_file_name, 'w') as destination_file:
        for line_number, line in enumerate(source_file, start=1):
            if line_number == 1:
                destination_file.write("\t".join(map(lambda text: text.ljust(20),title_first_line))+"\n")
                destination_file.write("\t".join(map(lambda text: text.ljust(20),title_second_line))+"\n")
            if line_number<actual_data_start_from:
                continue
            destination_file.write(f"{get_destination_file_content(line,t_value)}\n")
            t_value= t_value + increment_by
            actual_starting_line = actual_starting_line+1

