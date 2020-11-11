from Bio import Entrez, SeqIO


def main():

    # Coordonnées pour NCBI Entrez
    Entrez.email = 'mathieu@mathieulemieux.com'

    # Message d'accueil
    print("""Bienvenu au programme de recherche de gène par mot-clé!""")

    # Recherche de gène par mot-clé
    IdList = rechercherGene()

    if len(IdList) != 0:
        # Choix d'un gène parmi la liste
        index = choisirGene(IdList)
        # Téléchargement de la séquence nucléotidique de référence (RefSeq) du gène choisi
        telechargerSequenceADN(IdList[index])


def rechercherGene():
    
    # Interroger l'utilisateur
    organism, keyword = None, None
    while not organism: organism = input("""Spécifiez un organisme: """).strip()  # <- J'ai ajouté le choix de l'organisme; c'est optionnel!
    while not keyword : keyword  = input("""Spécifiez un mot-clé: """).strip()

    # ESearch - Recherche par mot-clé
    term   = f'{organism}[organism] {keyword}*[gene]'
    handle = Entrez.esearch(term=term, db='gene', retmax='5', sort='relevance')
    record = Entrez.read(handle)
    handle.close()

    # Retourne la liste des identifiants des gènes
    IdList = record['IdList']
    return IdList


def choisirGene(IdList):

    # ESummary - Obtention des informations sur les gènes de la liste
    handle    = Entrez.esummary(db='gene', id=','.join(IdList))
    record    = Entrez.read(handle)
    summaries = record['DocumentSummarySet']['DocumentSummary']
    handle.close()

    # Afficher la liste des gènes (avec index et description)
    for i in range(len(IdList)): print(i, summaries[i]['Description'], sep='. ')
    
    # Interroger l'utilisateur
    choix = -1
    while choix not in range(len(IdList)):
        choix = input("""Choisissez un gène parmi la liste retournée: """)
        if choix.isnumeric(): choix = int(choix)

    # Retourne l'index du gène choisi dans la liste des gènes
    return choix


def telechargerSequenceADN(IdGene):

    # ELink - Obtention de la référence croisée
    handle   = Entrez.elink(dbFrom='gene', db='nuccore', id=IdGene, linkname='gene_nuccore_refseqgene')
    record   = Entrez.read(handle)
    idRefSeq = record[0]['LinkSetDb'][0]['Link'][0]['Id']
    handle.close()

    # EFetch - Obtention de la séquence au format Fasta
    handle = Entrez.efetch(db='nuccore', id=idRefSeq, rettype='fasta')
    record = SeqIO.read(handle, 'fasta')
    handle.close()

    # Enregistrement du fichier Fasta
    fileName = f"{record.id}.fasta"
    SeqIO.write(record, fileName, 'fasta')
    print("Séquence téléchargée!")




# Call Main()
if __name__ == '__main__': main()