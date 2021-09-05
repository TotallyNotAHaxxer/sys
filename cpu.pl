use System::Info qw<sysinfo>; 

my $si = System::Info->new;

printf "Processor Type ==> %s\n", $si->cpu_type;