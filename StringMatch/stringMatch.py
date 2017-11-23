# make a function for matching the string

N="TAG"
K="L"
D="E"

g4 = 'NKXD'
protein = 'TQIEHKSDNQIETLSDNKSDNKADMASEIHMTGPMCLIENTNGRLMANPEALKILSAITQPMVVVAIVGLYRTGKSYLMNKLAGKKKGFSLGSTVQSHTKGIWMWCVPHPKKPGHILVLLDTEGLGDVEKGDNQNDSWIFALAVLLSSTFVYNSIGTINQQAMDQLYYVTELTHRIRSKSSPDENENEVEDSADFVSFFPDFVWTLRDFSLDLEADGQPLTPDEYLTYSLKLKKGTSQKDETFNLPRLCIRKFFPKKKCFVFDRPVHRRKLAQLEKLQDEELDPEFVQQVADFCSYIFSNSKTKTLSGGIQVNGPRLESLVLTYVNAISSGDLPCMENAVLALAQIENSAAVQKAIAHYEQQMGQKVQLPTETLQELLDLHRDSEREAIEVFIRSSFKDVDHLFQKELAAQLEKKRDDFCKQNQEASSDRCSALLQVIFSPLEEEVKAGIYSKPGGYRLFVQKLQDLKKKYYEEPRKGIQAEEILQTYLKSKESMTDAILQTDQTLTEKEKEIEVERVKAESAQASAKMLQEMQRKNEQMMEQKERSYQEHLKQLTEKMENDRVQLLKEQERTLALKLQEQEQLLKEGFQKESRIMKNEIQDLQTKMRRRKACTIS'

def g4_match(g4,protein):

    spl_mismatch, mismatch = (0,0)

    for x,y in zip(g4,protein):

        if (x == 'N'):
            if (y == 'N'):
                pass
            elif (y != 'N' and y in 'TAG'):
                spl_mismatch+=1
            else:
                mismatch+=1

        if (x == 'K'):
            if (y == 'K'):
                pass
            elif (y != 'K' and y in 'LQ'):
                spl_mismatch+=1
            else:
                mismatch+=1

        if (x == 'X'):
            pass

        if (x == 'D'):
            if (y == 'D'):
                pass
            elif (y == 'E'):
                spl_mismatch+=1
            else:
                mismatch+=1

    if mismatch > 0 or spl_mismatch > 2:
        return False

    return True


print g4_match(g4,protein)
