def dna_errors(seq1, seq2):
    seq_d1=list(str(seq1.upper()))
    seq_d2=list(str(seq2.upper()))
    at=["A","T"]
    cg=["C","G"]
    number=0
    for i in range (min(len(seq_d1),len(seq_d2))):
        try_list=[]
        try_list.append(seq_d2[i])
        try_list.append(seq_d1[i])
        if try_list!=at and try_list!=cg:
            number+=2
            if "-" in try_list:
                if try_list==["-","-"]:
                    number=number
                else:
                    number-=1
    number+=abs(len(seq_d1)-len(seq_d2))
    return(number)



def main():
    seq_1=input("what's the first sequence: ")
    seq_2=input("what's the second sequence: ")
    print(dna_errors(seq_1,seq_2))


if __name__ == "__main__":
    main()
