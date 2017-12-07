import csv

def match(X,Y):
    mismatch = 0
    for x,y in zip(X,Y):
            if not (x == 'X' or x == y):
                mismatch += 1

    #print(mismatch)
    if mismatch > 1:
        return False
    return True

def g4_match(X,Y):

    N = "NTAG"
    K = "KLQ"
    D = "DE"

    spl_mismatch, mismatch = (0,0)
    # for x,y in zip(X,Y):
    #     if ('N' != y):
    #         if (y == 'T' or y == 'A' or y == 'G'):
    #             spl_mismatch+=1
    #     elif ('K' != y):
    #         if (y == 'L' or y == 'Q'):
    #             spl_mismatch+=1
    #     elif ('D' != y):
    #         if (y == 'E'):
    #             spl_mismatch+=1

    for x,y in zip(X,Y):
        if not (y in "NKXD"):
            if (x == 'N' and y in N):
                spl_mismatch+=1
            elif(x == 'K' and y in K):
                spl_mismatch+=1
            elif(x == 'X'):
                spl_mismatch+=0
            elif(x == 'D' and y in D):
                spl_mismatch+=1
            # else:
            #     mismatch+=1

    if mismatch > 0 or spl_mismatch > 2:
        return False

    return True

#print g4_match(g4,protein)


def H(protein,x1,x2,x3,x4):

        def find_matches(x,g4_match):
            match_positions = []
            matches         = []
            for i in range(len(protein) - len(x)):
                candidate = protein[i : i + len(x)]
                if match(x, candidate):
                    match_positions.append(i)
                    matches        .append(candidate)
                elif g4_match(x, candidate):
                    match_positions.append(i)
                    matches        .append(candidate)
            #print("Mmatches: ",matches, match_positions)
            return matches, match_positions

        L1, pL1 = find_matches(x1, match)
        L2, pL2 = find_matches(x2, match)
        L3, pL3 = find_matches(x3, g4_match)
        L4, pL4 = find_matches(x4, match)
        #print L1, pL1
        #print L2, pL2
        #print L3, pL3
        #print L4, pL4

        candidates = []
        for a in zip(pL1, L1):
            for b in zip(pL2, L2):
                for c in zip(pL3, L3):
                    for d in zip(pL4, L4):
                        if (40 <= b[0] - a[0] <= 80 and
                            40 <= c[0] - b[0] <= 80 and
                            20 <= d[0] - c[0] <= 80    ):
                            #print(a,b,c,d)
                            candidates.append((a,b,c,d))
                        elif (80 <= b[0] - a[0] <= 120 and
                              40 <= c[0] - b[0] <= 80 and
                              120 <= d[0] - c[0] <= 180 ):
                            #print(a,b,c,d)
                            candidates.append((a,b,c,d))
                        elif (40 <= b[0] - a[0] <= 80 and
                              80 <= c[0] - b[0] <= 80 and
                              120 <= d[0] - c[0] <= 180 ):
                            #print(a,b,c,d)
                            candidates.append((a,b,c,d))


            with open('output_2.csv', 'a') as myfile:
                wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                #wr.writerow([pdb_id])
                #wr.writerow([protein_name])
                wr.writerow([protein])
                #wr.writerow([source])
                for i in candidates:
                    wr.writerow([i])

g1 = 'GXXXXGK'
g3 = 'DXXG'
g4 = 'NKXD'
g5 = 'EXSAX'

protein = 'MASEIHMTGPMCLIENTNGRLMANPEALKILSAITQPMVVVAIVGLYRTGKSYLMNKLAGKKKGFSLGSTVQSHTKGIWMWCVPHPKKPGHILVLLDTEGLGDVEKGDNQNDSWIFALAVLLSSTFVYNSIGTINQQAMDQLYYVTELTHRIRSKSSPDENENEVEDSADFVSFFPDFVWTLRDFSLDLEADGQPLTPDEYLTYSLKLKKGTSQKDETFNLPRLCIRKFFPKKKCFVFDRPVHRRKLAQLEKLQDEELDPEFVQQVADFCSYIFSNSKTKTLSGGIQVNGPRLESLVLTYVNAISSGDLPCMENAVLALAQIENSAAVQKAIAHYEQQMGQKVQLPTETLQELLDLHRDSEREAIEVFIRSSFKDVDHLFQKELAAQLEKKRDDFCKQNQEASSDRCSALLQVIFSPLEEEVKAGIYSKPGGYRLFVQKLQDLKKKYYEEPRKGIQAEEILQTYLKSKESMTDAILQTDQTLTEKEKEIEVERVKAESAQASAKMLQEMQRKNEQMMEQKERSYQEHLKQLTEKMENDRVQLLKEQERTLALKLQEQEQLLKEGFQKESRIMKNEIQDLQTKMRRRKACTIS'
H(protein,g1,g3,g4,g5)
