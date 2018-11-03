=pod
Solution to the FIB Rosalind problem - a modified fibonacci algorithm
Author: Peter Vlasveld
=cut

#!/usr/bin/perl
use strict;
use warnings;

#take in data from file
open(IN, "rosalind_fib.txt") or die "Couldn't open input file";
my $data = <IN>;
close IN;

#splitinput values into array
my @input = split / /, $data;

#print output of fibonacci algorithm to console
print fibo($input[0],$input[1]), "\n";

#modified fibonacci algorithm to allow for k rabbit pairs per month rather than just 1
sub fibo{
	my ($num,$pairs) = @_;
	if ($num == 0) { return 0; }
	if ($num == 1) { return 1; }
	my $result = fibo($num-1,$pairs);
	
	$result += (fibo($num-2,$pairs))*$pairs;
	
	return $result;
}
