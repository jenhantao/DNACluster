DNACluster
==========

analyzes DNA clustering data

Want to do: verify primer design for gene synthesis.  Specifically,
this is to check that the non-pair primers don't have too much
homology

Input: dnaclust (http://dnaclust.sourceforge.net/)  file of clusters
of dna sequences (these could be protein as well i guess)
note how the input has #2 if the cluster has two dna sequences, and #1
if it has one

output/options: strip the file of all #1, {1, 2}, or {1, ..., n}
clusters (maybe we don't care about sequenecs that don't cluster with
other sequences
an example input is attached

another option is to write out to a file, or create a new directory
where you split out each cluster into a file (and remove the #n line)


Basically, these are oligos that are being designed by my software.
we need to then check that there isn't too much oligo
cross-hybridization.  Later on, we can do some bioinformatics-y stuff
like check there are no stem loops or have an output format that looks
like clustalw (it's way easier for humans to check that there are a
certain # of mismatches, etc)...   Eventually this will be put into
clotho.  CHris says it's okay to write it in python b/c java has some
sort of python wrapper?  Anyways, i don't want to get into clotho, so
writing it in python would be better.


example of clustalw format
(http://www.ebi.ac.uk/Tools/services/web_clustalw2/toolresult.ebi?tool=clustalw2&jobId=clustalw2-I20120915-184728-0093-65193372-pg)
note how the matches/mismatches are explicitly stated, unlike in fasta
alignment format

for muscle executable
http://www.drive5.com/muscle/
