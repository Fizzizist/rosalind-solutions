=pod
Solution to PERM Rosalind problem
Generates permutations from 1 to n and totals them
Author: Peter Vlasveld
=cut

#!/usr/bin/perl

use strict;
use warnings;

#Get number from file
open(IN, "rosalind_perm.txt") or die "Couldn't open the file";
my $number = <IN>;
close IN;

#create number array
my @array = (1..$number); 

#create global variable for return array
my @finalArr = ();

#open output file for writing
open(OUT, ">output.txt") or die "Couldn't open output file";

#print result of perm subroutine
print OUT perm(\@array, 0), "\n";

#print array of permutations
for (@finalArr){
	print OUT "@{$_}\n";
}

#close output file
close OUT;

#Recursive permutation subroutine
sub perm{
	#declare sub variables
	my ($arr_ref, $num) = @_;
	my $count = 0;
	#dereference input array
	my @arr = @{$arr_ref};
	
	#base case - when num = length of array
	if ($num == $#arr) {
		push @finalArr, \@arr;
		return 1;
	}
	else 
	{
		#perform a swap of num and each other number in the array, and then call the next instance of the sub
		for ($num..$#arr){
			($arr[$num], $arr[$_]) = ($arr[$_], $arr[$num]);
			$count += perm(\@arr, $num+1);
		}
		#eventually returns number of permutations
		return $count;
	}
}
