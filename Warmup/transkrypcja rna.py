"""
RNA transcription
"""


transcription = {
    'G':'C',
    'C':'G',
    'T':'A',
    'A':'U',
}

def transcribe_rna(dna):
    """
    Transcribe RNA
    :param dna:
    :return: rna
    """
    rna = ''
    for letter in dna:
        rna += transcription[letter]
    return rna
def validate_dna(dna):
    """
    Validate DNA
    :param dna: 
    :return: 
    """
    return set(dna).issubset(set('GCTA'))

def main():
    """
    Main function
    :return:
    """
    while True:
        my_dna = input('Type DNA sequence: ')
        my_dna = my_dna.upper()
        if not validate_dna(my_dna):
            answer = input('Invalid DNA sequence, try again ([y]/n)')
            if answer.lower() != 'y':
                break
            continue
        rna = transcribe_rna(my_dna)
        print((f'Transcibed RNA: {rna}'))
        return

if __name__ =='__main__':
    main()

    #input_dna = input('Provide DNA ')
    #input_dna = input_dna.upper()


    #print(transcribe_rna(input_dna))