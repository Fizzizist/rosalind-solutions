=pod
Solution to the Rosalind REVC problem
Author: Peter Vlasveld
=cut

#!/usr/bin/perl
use strict;
use warnings;
use Switch;

#take in dataset
open(IN, "rosalind_revc.txt") or die "Couldn't open input file";
my $dataset = <IN>;
close IN;

#split data into single letters
my @dna = split //, $dataset;

#declare complement array
my @complement;

#make complement array which corresponds to @dna array
for (@dna){
	switch($_){
		case 'A' { push @complement, 'T'; }
		case 'T' { push @complement, 'A'; }
		case 'G' { push @complement, 'C'; }
		case 'C' { push @complement, 'G'; }
	}
}

#reverse the complement
@complement = reverse @complement;

#join back into a single string and output to a file
my $result = join '', @complement;
open(OUT, ">outlog.txt") or die "couldn't open output file";
print OUT $result;

#print solution to console
print "$result\n";
