=pod
Solutions to GRPH Rosalind problem
Author: Peter Vlasveld
=cut

#!/usr/bin/perl
use common::sense;

#take in data
open(IN, "rosalind_grph.txt") or die "Couldn't open input file";
my @data = <IN>;
close IN;

#declare variables
my (@headers, @DNA, @result);
my $temp = "";

#convert FASTA data into array of DNA strings and headers
for (@data){
	unless (substr($_,0,1) eq '>'){
		$temp .= substr($_,0,-1);	
	} else {
		push @headers, substr($_,0,-1);
		push @DNA, $temp;
		$temp = "";
	}
}
push @DNA, $temp;
shift @DNA;
#print @headers,"\n",@DNA,"\n";

#write which headers overlap to @result
for my $i (0..$#DNA){
	for my $j (0..$#DNA){
		print "$DNA[$i]$DNA[$j]\n";
		if ($DNA[$i] eq $DNA[$j]) { next; }
		elsif (substr($DNA[$i],-3) eq substr($DNA[$j],0,3)){
			push @result, substr($headers[$i],1)." ".substr($headers[$j],1);
		}
	}
}

#print result to file
open(OUT, ">output.txt") or die "Couldn't open output file";
for (@result){
	print OUT $_,"\n";
}
close OUT;
	
