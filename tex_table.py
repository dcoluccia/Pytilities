"""
Write a TeX table given numpy array input.

@author: ColucciaD
"""
import os, subprocess
###############################################################
def write_table(col_names,
                row_names,
                content,
                name = 'table'):
    """
    Write in a TeX file a table which can then
    seemlessly be imported into the main TeX file
    using an \input{} command.
    NOTE: add booktabs to your TeX file.
    
    Parameters
    -------------
    col_names   : list (len(.) = C)
                    A list that contains all
                    names in the columns
    row_names   : list (len(.) = R)
                    A list that contains all
                    names in the rows
    content     : np.array (shape(content) = [R,C])
                    A np.array that stores the
                    inner entries of the table.
    
    Output
    -------------
    name.tex    : .tex file
                    A tex file that encodes the
                    entries.
    """
    # name of the file
    name_file = name + '.tex'
    
    # number of columns in the table
    index_cols = (len(col_names)+1) * 'c' # number of columns in the table
    index_cols = '{'+index_cols+'}'
    
    # header of the table
    args   = {'table'   :'{table}',
              'tabular' :'{tabular}',
              'arg0'    : index_cols}
    header = '''\
                \\begin{table}[h]       
                \\centering             
                \\begin{tabular}{arg0}    
                \\toprule                
            '''.format(**args)
    
    # first line with the names of the variables
    first_line = '& '
    for j in range(len(col_names)):
        arg = {'arg0' : '{' + str(col_names[j]) + '}'}
        first_line = first_line + '''\\textsc{arg0} & '''.format(**arg)          
    first_line = first_line[:-2]
    first_line = first_line + '\\\\ '
    first_line = first_line + '\\midrule  '
    
    # populate the main content of the table
    main = []
    for i in range(len(row_names)):
        arg  = {'arg0' : '{' + row_names[i] + '}'}
        line = '\\textsc{arg0} & '.format(**arg)
        for j in range(len(col_names)):
            arg  = {'arg0' : str(content[i][j])}
            line += '${arg0}$&'.format(**arg)
        line = line[:-1]
        line += '\\\\ '
        main.append(line)
    
    # footer of the table
    args   = {'table'       :'{table}',
              'tabular'     :'{tabular}',
              'Caption'    : '{Insert caption here.}'}
    footer = '''\
                \\bottomrule            
                \\end{tabular}          
                \\caption{Caption} 
                \\end{table}            
            '''.format(**args)
    
    # put everything together
    text = header + first_line
    for i in range(len(main)):
        text += main[i]
    text += footer
    
    # delete files with the same name
    if os.path.exists("{}".format(name_file)) == True:
            os.remove("{}".format(name_file))

    # Write the new file
    with open('{}'.format(name_file),'w') as f:
         f.write(text)
###############################################################