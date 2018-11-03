=pod
Solution to IPRB Rosalind problem
Author: Peter Vlasveld
=cut

#!/usr/bin/perl
use strict;
use warnings;

#take in data from file
open(IN, "rosalind_iprb.txt") or die "Couldn't open input file";
my $data = <IN>;
close IN;

#split dataset into array
my @dataset = split / /, $data;

#calculate total probability ratios
my $total = $dataset[0] + $dataset[1] + $dataset[2];
my $initmRatio = $dataset[1]/$total;
my $initnRatio = $dataset[2]/$total;

#calculate values of progeny from probability ratios and population data 
my $sameHeteroDom = ($initmRatio * (($dataset[1]-1)/($total-1)))*0.25;
#print $sameHeteroDom, "\n";
my $oneAndOne1 = ($initmRatio * ($dataset[2]/($total-1)))*0.5;
#print $oneAndOne1, "\n";
my $oneAndOne2 = ($initnRatio * ($dataset[1]/($total-1)))*0.5;
#print $oneAndOne2, "\n";
my $sameHeteroRec = $initnRatio * (($dataset[2]-1)/($total-1));
#print $sameHeteroRec, "\n";

#calculate resulting progeny
my $result = 1-($sameHeteroDom + $oneAndOne1 + $oneAndOne2 + $sameHeteroRec);

#output result to console
printf("%.5f\n", $result);
