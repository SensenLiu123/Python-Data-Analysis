"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    if line1==line2:
        return IDENTICAL
    minlength=min([len(line1),len(line2)])
    for i in range(minlength):
        if line1[i] ==line2[i]:
            if i ==minlength-1:return minlength
            continue
        return i
        


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    if '\n' in line1+line2 or '\r' in line1+line2:
        return ""
    minlength=min([len(line1),len(line2)])
    if idx > minlength-1:return ""
    string = line1+'\n'+'='*idx+'^\n'+line2
    return string


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    if line1==line2:
        return (IDENTICAL, IDENTICAL)
    minlength=min([len(lines1),len(lines2)])
    for i in range(minlength):
        if lines1[i] ==lines2[i]:
            if i ==minlength-1:return (minlength,0)
            continue
        else: return (i,singleline_diff(lines1[i], lines2[i]))
    


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    handle = open(filename,'rt')
    llist = []
    for line in handle:
        this_line = line.rstrip()
        llist.append(this_line)
    handle.close()    # This is crucial
    return llist


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    lines1 = get_file_lines(filename1)
    lines2 = get_file_lines(filename2)
    dif_list = multiline_diff(lines1, lines2) # tuple
    string = 'Line {}:\n'.format(dif_list[0])
    string+=singleline_diff_format(lines1[dif_list[0]], lines2[dif_list[0]], dif_list[1]):
    return string