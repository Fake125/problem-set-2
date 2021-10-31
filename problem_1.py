import re
def fill_spaces(line,max):
    if len(line) == max:
        return line
    spaces_indices = []
    for match in re.finditer(' ', line):
        spaces_indices.append(match.start())
    if len(spaces_indices) == 0:
        for i in range(len(line),max):
            line = line + " "
        return line
    space_turn = 0
    while len(line) <=max-1:
        line = line[:spaces_indices[space_turn]] + " " + line[spaces_indices[space_turn]:]
        if space_turn != len(spaces_indices)-1:
            for i in range(space_turn,len(spaces_indices)-1):
                spaces_indices[i+1] = spaces_indices[i+1]+1
        if space_turn == len(spaces_indices)-1:
            space_turn = 0
        else:
            space_turn = space_turn+1
    return line

def justify(str,max):
    new_line = ""
    counter = 0
    lines = []
    while counter < len(str):
        new_word = ""
        if len(new_line) > 0:
            new_word = " "
        new_word = new_word  + str[counter]
        weight = new_line + new_word
        if len(weight) <= max:
            new_line = weight
            counter = counter+1
            if counter == len(str):
                lines.append(new_line)
        else:
            lines.append(new_line)
            new_line =""
    return lines

class Solution:
    def fullJustify(self,str,max):
        lines = justify(str,max)
        new_lines = []
        counter = 0
        for l in lines:
            if counter == len(lines)-1:
                for i in range(len(l),max):
                    l = l + " "
            new_lines.append(fill_spaces(l,max))
            counter = counter+1
        return new_lines    
