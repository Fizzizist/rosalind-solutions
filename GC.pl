=pod
Solution to GC Rosalind problem
Author: Peter Vlasveld
=cut

#!/usr/bin/perl
use strict;
use warnings;

#take in data from file
open(IN, "rosalind_gc.txt") or die "Couldn't open input file";
my @data = <IN>;
close IN;

#declare variables
my @ID;
my @sequences;
my @tempArr;
my $finalID;
my $finalPerc = 0;

#add first @data line to @ID
$ID[0] = $data[0];

#loop through 1..$#data
for (1..$#data){
	#when a line starts with >, 
	if (substr($data[$_],0,1) eq '>'){
		#add it to @ID, join the temp array and add it to @sequences
		push @ID, $data[$_];
		my $temp = join ('', @tempArr);
		push @sequences, $temp;
		@tempArr = undef;
	} else {
		#add line to temp array
		push @tempArr, $data[$_];
	}
}

#join last temp and add to sequences
my $temp = join('', @tempArr);
push @sequences, $temp;

#loop through @sequences
for (0..$#sequences){
	$sequences[$_] =~ s/\s//g;
	print $sequences[$_];
	#declare percentage
	my $percentage;
	my $GC;
	my $total = length $sequences[$_];
	#determine percentage of GC in the sequence
	$GC = ($sequences[$_] =~ tr/GC//);
	$percentage = ($GC/$total)*100;
	print "$percentage\n";
	#if percentage is greater than finalPerc, then finalPerc eq percentage and finalID eq ID
	if ($percentage>$finalPerc) {
		$finalPerc = $percentage;
		$finalID = $ID[$_];
	}
}

#output id and percent
printf("%s%f\n", $finalID, $finalPerc);


