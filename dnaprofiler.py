#DNA PROFILER: determine which STR profiles match a given sequence of DNA
    #first define longest_str_repeat_count, then define find_match, then define read_strs, get_strs, last  dna_match. 
    #dna_match function = 1. find a match 
    #the STR database in a file named str_profiles.csv and four DNA files
    #use csv.DictReader
    #open DNA sequence file and read its contents into memory
    #For each of the STRs,  compute the longest run of consecutive repeats of the STR in the DNA sequence we need to identify
    #the STR counts match exactly with any of the individuals in the CSV file, your program should print out the name of the matching individual
       #if str_counts == file.cvs.element; print(name of individual)  else: print(no match)      
import csv

def read_dna(dna_filename):
    with open(dna_filename, "r") as text_file:
        data = text_file.read()
        return data
    pass

def dna_length(dna_filename):
   return len(read_dna(dna_filename))
   pass


def read_strs(dna_filename):
    with open(dna_filename) as text_file: 
        csv_file = csv.DictReader(text_file)
        result = []
        for line in csv_file:
            result.append(line)
        return result
    pass

def get_strs(dict):
    result = []
    for k,v in dict.items():
        if k != 'name':
            result.append((k, int(v)))
    return result
    pass


def longest_str_repeat_count(str_frag, dna_seq):
    i = 0
    preindex = 0
    index = 0
    while i < len(dna_seq):
        if dna_seq[i:i+4] == str_frag:
                index += 1
                if index > preindex:
                    preindex = index
                i += 4
        elif dna_seq[i:i+4] != str_frag:
                if index > preindex:
                    preindex = index
                i += 1 
                index = 0
    print(preindex)  
    pass     

def find_match(str_profile, dna_seq):
    setinfo = longest_str_repeat_count(str_profile, dna_seq)
    if setinfo == str_profile:
        print('True')
    else:
        print("False")
    pass            

        
def dna_match(str_filename, dna_filename):
    pass
    
            
            #if dna_seq[i:i+4] == str_frag:
            #    index += 1
            #else:

            #index = dna_seq.split('AGAT')
          #  print(index)
            #break


#    list = str(dna_seq)
#    index = list.find(str_frag)
#    print(index)


# We check if this module is the "main" module. If it is, we run the
# code inside of the `if` block.
if __name__ == '__main__':
    profiles = read_strs('str_profiles.csv')
    assert(get_strs(profiles[0])[0] == ('AGAT', 5))
