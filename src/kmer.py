"""Computing kmers of a string."""


def kmer(x: str, k: int) -> list[str]:
    """
    Computer all k-mers of x.

    >>> kmer('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']

    FIXME: do you want more tests here?
    """
    if k<=0:
        raise Exception("Stupid k")
    return [i:i+k] for i in range(len(x)-k+1)
    #assert(k>=1)
    ...


def unique_kmers(x: str, k: int) -> list[str]:
    """
    Computer all unique k-mers of x.

    FIXME: do you want more tests here?
    """
    result=[] #result=set()
    kmers=kmer(x,k)
    for kmer in kmers:
        if kmer not in result:
            result.append(kmer) #result.add(kmer)
    return result #list(result)
    #return list(set(kmers(x,k))) - set() finder alle unikke elementer, så denne linje virker alene
    ...


def count_kmers(x: str, k: int) -> dict[str, int]:
    """
    Computer all k-mers of x and count how often they appear.

    FIXME: do you want more tests here?
    """
    kmer_dict={}
    kmers=kmer(x,k)
    for kmer in kmers:
        if kmer not in kmer_dict:
            kmer_dict[kmer]=0
        kmer_dict[kmer]+=1
    #y=[(v,k) for k,v in kmer_dict.item()]
    #y.sort
    #return y
    return kmer_dict

    ...
