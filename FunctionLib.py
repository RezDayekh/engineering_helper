def fix_path(path):
    '''this function takes a string in raw format and fixes it to reference the right link'''
    split_the_path = path.split('\\')
    #check every split for the cahracter '\x01' 
    for one_split in split_the_path:
        for char_in_split in one_split:
            if char_in_split == '\x01':
                one_split = one_split.split(char_in_split)
                split_the_path[-1] = one_split[0]
                job_number = '1' + one_split[-1]
                split_the_path.append(job_number)

    new_path = ''
    for i in range(0,len(split_the_path)):
        if split_the_path[i] != split_the_path[-1]:
            new_path = new_path + split_the_path[i] + '\\'
        else:
            new_path = new_path + split_the_path[i]

    return new_path