# Lina Kang
# 1072568
# HW 03 PS 4 - Genome String

def checkGenome(genome):

    # find where the gene starts - ATG
    index = genome.find("ATG")

    if index == -1:
        print("no gene is found")
    else:
        while index != -1:
            
            # locate where exactly the gene begins (after G of ATG)
            firstIndex = index + 3
            
            subgenome = genome[firstIndex:]

            # find all three end points: TAG, TAA, TGA
            lastIndex1 = subgenome.find("TAG")
            lastIndex2 = subgenome.find("TAA")
            lastIndex3 = subgenome.find("TGA")

            lastIndices = [lastIndex1, lastIndex2, lastIndex3]
            
            loop = len(lastIndices)

            # determine which end point comes first
            while loop != 0:
                lastIndex = min(lastIndices)
                if lastIndex == -1: # in the case this endpoint does not exist 
                    lastIndices.remove(lastIndex)
                    loop = loop - 1
                else:
                    loop = 0
            
            lastIndex = firstIndex + lastIndex # because lastIndex is an index of the subgenome, not the actual genome string

            # extract the new found gene
            gene = genome[firstIndex:lastIndex]
            print(gene)

            # create a new gene starting from the point after the new found gene
            genome = genome[lastIndex+3:]

            index = genome.find("ATG")


def main():
    genome = input("Enter a genome string: ")
    checkGenome(genome)

    
if __name__ == "__main__":
    main()

## Test Case 1.
##
##Enter a genome string: TTATGTTTTAAGGATGGGGCGTTAGTT
##TTT
##GGGCGT
##
## Test Case 2.
##    
##Enter a genome string: TGTGTGTATAT
##no gene is found
##
## Test Case 3.
##
##Enter a genome string: TGATGCTCTAAGGATGCGCCGTTGATT 
##CTC
##CGCCGT
## 
## Test Case 4.
## 
##Enter a genome string: TGATGCTCTAGAGATGCGCCGTTGAATAT 
##CTC
##CGCCGT
##
## Test Case 5.
## 
##Enter a genome string: TGATGCGTCTAAGAGACTGCTCGCCGGTTGAATAT
##CGTC
##
## Test Case 6.
##
##Enter a genome string: TGATGGCTCCTATGAGAATGGCGCCCGTTTCGAAATAT
##GCTCCTA
##
