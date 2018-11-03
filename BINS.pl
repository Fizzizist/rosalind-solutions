=pod
Binary search program for solving Rosalind BINS problem
Author: Peter Vlasveld
=cut
#!/usr/bin/perl
use strict;
use warnings;

#take in data
open(IN, "rosalind_bins.txt") or die "Couldn't open the input file";
my @data = <IN>;
close IN;

#declare and fill data arrays
my @list = split / /, $data[2];
my @keys = split / /, $data[3];

#declare arrays
my (@outArr, @test);

#run binary searches and store in @outArr
for (@keys){
	my $result = binSearch($_,\@list,0,$#list);
	push(@outArr, $result);
}

#join search results into one string
my $outStr = join(' ', @outArr);

#open file and print output to it
open(OUT, ">outlog.txt") or die "Couldn't open the output file";
print OUT $outStr;
close OUT;

#also print the output to the console
print $outStr, "\n";

#binary search algorithm
sub binSearch{
	my ($key, $list_ref, $left, $right) = @_;

	if ($left > $right) { return -1; }
	
	my $middle = int(($left + $right) / 2);
	print "$middle\n";
	my @array = @{$list_ref};
	
	if ($array[$middle] == $key) { return int($middle)+1; }
	elsif ($array[$middle] > $key) {
		return binSearch($key, $list_ref, int($left), int($middle-1));
	}else{
		return binSearch($key, $list_ref, int($middle+1), int($right));
	}
}
