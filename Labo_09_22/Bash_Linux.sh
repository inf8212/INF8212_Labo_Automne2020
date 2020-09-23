################################################################################################################
# Commandes LINUX courantes
# Mathieu Lemieux
# Automne 2020
################################################################################################################


# CONFIGURATION / INSTALLATION DE PACKAGES
#########################################

	# Connaitre sa version d'Ubuntu
	lsb_release -a
	uname -r        # Version de Windows...

	# Update the source listing
	sudo apt-get update

	# Connaitre les versions de package (disponibles?)
	apt-cache madison <package_name>

	# Installer une version specifique
	sudo apt-get install <package_name>=<package_version> -V

	# Installer une application via fichier .deb (build deja fait pour une version specifique de Linux)
	sudo dpkg -i /path/to/deb/file
	sudo apt-get install -f
	
	# Activation/Deactivation par defaut de Anaconda
	conda config --set auto_activate_base False or True
	
	# Liste de tous les packages dans un environnement virtuel
	pip freeze > requirements.txt
	# Installation des packages requis
	pip install -r requirements.txt


	

# NAVIGATION DANS LES DOSSIERS
#########################################

	# PWD
	# Pour connaitre le chemin complet du répertoire courant
	pwd

	# CD
	# Pour se déplacer dans l'arborescence des dossiers
	cd <nom_de_dossier>
	cd ..    											# Remonter en amont, 1 dossier
	cd ../.. 											# Remonter en amont, 2 dossiers

	# LS / DIR
	# Lister le contenu d'un dossier
	# Les options '-l' et -'al' pernettent de voir plus de détails...
	ls -al                               # Dossier courant (option '-la' pour voir les fichiers/dossiers cachés)
	ls /../dossier                       # Dossier distant (sans s'y déplacer)
	# La commande 'dir' (comme sous Windows) fonctionne aussi...
	dir

	# MKDIR
	# Créer un nouveau dossier
	mkdir test												 	# Dans le répertoire courrrant
	cd !$				                                        # Se déplacer dans le dossier que l'on vient juste de créer. '!$' Executes cd on the last argument of the previous command.
	mkdir /home/.../test 	                                    # Avec chemin absolut
	mkdir ../test											 	# Avec chemin relatif
	mkdir test test/data test/scripts test/results			 	# Plusieurs dossiers/sous-dossiers à la fois
	# Going crazy...
	mkdir sa{1..50}												# 50 directories from sa1 through sa50
	mkdir -p sa{1..50}/sax{1..50}								# same but each of the directories will hold 50 times sax1 through sax50. '-p' will create parent directories if they do not exist.
	mkdir {a-z}12345 											# 26 directories from a12345 through z12345
	mkdir {1,2,3}												# comma separated list makes dirs 1, 2 and 3.
	mkdir test{01..10}											# 10 directories from test01 through test10.
	mkdir -p `date '+%y%m%d'`/{1,2,3}							# dossier avec la date (6 chiffres), dans lequel il y a les dossiers '1', '2' et '3'
	mkdir -p $USER/{1,2,3}										# same as 4 but with the current user as a directory and 1,2,3 in it.
	
	
# VISUALISER UN FICHIER
#########################################

	# LESS / MORE / ZLESS / ZMORE
	# Affiche le contenu, page par page
	# On entre 'q' pour quiter!!
	less file.txt     # Fichier non compressé - page par page avec Page up/down 
	more file.txt     # Fichier non compressé
	zless file.txt.gz # Fichier compressé - page par page avec Page up/down 
	zmore file.txt.gz # Fichier compressé

	# HEAD / TAIL
	# Affiche seulement le début/fin (10 lignes) d'un fichier non compressé
	head file.txt # Contenu du début
	tail file.txt # Contenu de la fin

	# CAT
	# Affiche tout le contenu
	# '-n' affiche le numéro de chaque ligne
	cat -n file.txt


# CREER / EDITER UN FICHIER
#########################################

	# TOUCH
	# Crée autant de fichiers (vides) à la fois qu'on veut
	touch file1.txt file2.txt

	# >
	# '>' c'est le 'redirect tool'. Ici on l'utilise pour rediriger vers un fichier inexistant qui va donc être créé.
	# Permet de créer 1 fichier (vide) à la fois
	> file.txt
	
	# CAT >
	# Pour créer un fichier et lui ajouter directement du contenu ligne par ligne. Si le fichier existe déjà, il va être écrasé !!
	# Touche 'Enter' pour enregistrer la ligne et passer à la suivante. 'Ctl-d' pour terminer
	cat > file.txt
	
	# GEDIT / NANO / VIM
	# Utiliser gedit pour une interface graphique (si activée), sinon nano ou vim
	nano file.txt
	# 'vim' ouvre le fichier avec l'éditeur vim (pas de GUI). Crée le fichier si inexistant.
	# Escape puis 'ZZ' pour sortir et sauvegarder les changements. 'ZQ' pour ignorer les changements
	vim file.txt


# MANIPULER LE CONTENU D'UN FICHIER
#########################################

	# Manipuler les lignes
	head -1000 input.txt > output.txt && sed -i '1,+999d' input.txt # Cut & Paste 1000 first rows from input.txt to output.txt
	head -1000 file.txt > first100lines.txt
	tail --lines=+1001 file.txt > restoffile.txt
	
	# Manipuler les caractères
	#....
	

# DEPLACER / RENOMER / COPIER
#########################################

	# MV
	# Pour déplacer/renommer des fichiers/dossiers.
	# Syntaxe 'mv [OPTIONS] source(s) destination'. Une ou plusieurs sources (dossier/fichier), une destination (dossier)
	# L'option '-v' affiche l'action performée au moment de l'exécution.
	# L'option '-i' demande confirmation avant exécution.
	mv -i file1.txt file2.txt data			        # Fichiers 'file1.txt' et 'file2.txt' déplacés dans dossier 'data' 
	# Pour renomer un fichier, on indique un seul fichier comme source, et son nouveau nom comme destination.
	# Attention, si le nouveau nom est déjà pris, le fichier va être ÉCRASÉ
	mv -i old_file_name.txt new_file_name.txt       # Fichier 'old_file_name.txt' renommé 'new_file_name.txt' 
	# Pour renomer/déplacer un dossier, on indique un seul dossier comme source, et son nouveau nom comme destination.
	# >> Si le nouveau nom est déjà pris, le dossier source va etre DÉPLACÉ dans le dossier destination.
	# >> Si le nouveau nom n'existe pas, le dossier source va etre RENOMMÉ.
	mv -i folder1 folder2                           # Dossier 'folder1' renommé 'folder2' ou déplacé dans 'folder2'
	
	# CP
	# Pour copier un fichier/dossier
	cp file.txt file_copy.txt						# Copie un fichier, avec un nouveau nom
	cp file1.txt file2.txt /backup					# Copie des fichiers dans un autre dossier
	cp -r data backup								# Copie un dossier (et tous ses fichiers et sous-dossiers)
	cp -rt data backup								# Copie le contenu d'un dossier (ses fichiers et sous-dossiers) mais pas le dossier lui-même
	
	# CAT <file-from> > <file-to>
	# Pour copier le CONTENU d'un fichier
	cat file1.txt > file2.txt						# Copy the contents of one file to another file. Le contenu du fichier destination va être écrasé!
	cat file1.txt >> file2.txt						# Append the contents of one file to the end of another file
	

# SUPPRIMER
#########################################

	# RM
	# Supprime les fichiers
	rm data/file.txt                 # Supprime le fichier 'file.txt' seulement
	rm data/file1.txt data/file2.txt # Supprime plusieurs fichiers à la fois
	rm data/*                        # Supprime tous les fichier du dossier 'data'
	rm *.txt					     # Supprime tous les fichier '.txt' du dossier courant
	# Supprime les dossiers
	rm -d data			             # Supprime le dossier 'data' si vide seulement
	rm -r data			             # Supprime le dossier 'data' vide ou non-vide (et tout son contenu)

	# RMDIR
	# Supprime les dossiers seulement.
	rmdir data

	# UNLINK
	# Supprime un fichier a la fois. Pas les dossiers.
	unlink data/file.txt
	

# COMPRESSER / DECOMPRESSER
#########################################

	# GZIP
	# Pour compresser individuellement 1+ fichier(s)
	# Option '-k' pour conserver le fichier original non compressé. Sinon SUPPRIMÉ
	# Options '-1' à '-9' pour le ratio de compression du min au max. -6 par défaut.
	gzip -k file1.txt file2.txt		# Va créer les fichiers 'file1.txt.gz' et 'file2.txt.gz'
	gzip -kr data					# Va créer 1 fichier '.gz' pour chaque fichier dans le dossier 'data'
	gzip -d file.txt.gz				# -d pour décompression du fichier
	gzip -dr data					# -dr pour décompression de tous les fichiers du dossier 'data'
	gzip -dr .						# -dr pour décompression de tous les fichiers du dossier courant
	gzip -l file.txt.gz				# -l pour les statistiques p/r au fichier compressé
	
	# GUNZIP
	# Décompresser fichier '.gz'.
	gunzip file.txt.gz
	
	# TAR
	# Compress an Entire Directory or Single/Multiple File(s). Fichier 'tarré'. Peut en plus être 'zippé' (option -z).
	# tar [OPTIONS] <archive_file_name.tar.gz> <file/folder_to_archive>
	# -c: Create an archive. -> fichier 'tarré'
	# -z: Compress the archive with gzip. -> fichier 'zippé'. On peut remplacer l'option -z par -j pour utiliser bzip2 au lieu de gzip.
	# -v: Display progress in the terminal while creating the archive, also known as “verbose” mode. The v is always optional in these commands, but it’s helpful.
	# -f: Allows you to specify the filename of the archive.
	tar -cvf name-of-archive.tar /dossier	# Compresser (.tar seulement) et enregistrer dans 'dossier'
	tar -czvf name-of-archive.tar.gz /dossier	# Compresser (.tar ET .gz) et enregistrer dans 'dossier'
	# Pour décompresser un fichier '.tar':
	tar -xvf archive.tar
	# Pour décompresser un fichier '.tar.gz':
	tar -xzvf archive.tar.gz					# Décompresser dans le dossier courant
	tar -xzvf archive.tar.gz -C /tmp			# Décompresser dans un autre dossier
	# Pour lister le contenu, option '-t'
	tar -tvf archive.tar.gz
	# Pour décompresser un seul fichier d'une archive
	tar -xvf archive.tar file1.txt				# Untar Single file from tar File
	tar -zxvf archive.tar.gz file1.txt			# Untar Single file from tar.gz File
	
	tar -cvf x.tar /x
	tar -xvf x.tar
	
	# ZMORE
	# Visualiser le contenu d'un fichier compressé
	zmore file.txt.gz


# UPLOAD / DOWNLOAD
#########################################

	# SCP
	# Pour importer/exporter des fichiers à partir/vers son PC (localhost): scp « quoi » « où »
	# Ouvrir un shell sur son ordi, idéalement à partir du dossier courant, puis utiliser la commande scp...


	# Copy file from a remote host to local host SCP example:
	scp username@from_host:file.txt /local/directory/
	# Copy file from local host to a remote host SCP example:
	scp file.txt username@to_host:/remote/directory/
	# Copy directory from a remote host to local host SCP example:
	scp -r username@from_host:/remote/directory/  /local/directory/
	# Copy directory from local host to a remote hos SCP example:
	scp -r /local/directory/ username@to_host:/remote/directory/
	# Copy file from remote host to remote host SCP example:
	scp username@from_host:/remote/directory/file.txt username@to_host:/remote/directory/


	# WGET
	# Pour importer des fichiers à partir d'une URL
	# Se déplacer dans le bon dossier, puis utiliser la commande wget...
	# Exemple:
	wget ftp://ftp.ncbi.nlm.nih.gov/1000genomes/ftp/release/20130502/ALL.chr2.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz


# AFFICHAGE A L'ECRAN
#########################################
	
	# export DISPLAY
	# Pour l'affichage graphique de certaines applications (ex. gedit)
	# (Alternativement à l'option '-Y' de la connexion ssh ?) on peut utiliser un Xserver (MobaXterm ou autre) et exporter le display
	# Attention, option compliquée et difficile à faire fonctionner sous Windows!
	export DISPLAY=:0
	export LIBGL_ALWAYS_INDIRECT=1
	
	
# AIDE
#########################################

	# HELP
	# Affiche l'aide sur une commande
	# --help
	<cmd> --help

	# INFO / MAN
	# Affiche la fiche d'information (info) ou le manuel (man) sur une commande.
	# Entrer 'q' pour quiter
	info <cmd>
	man <cmd>