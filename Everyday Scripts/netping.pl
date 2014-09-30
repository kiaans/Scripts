use Net::Ping;
$p = Net::Ping->new();
print "$host is alive.\n" if $p->ping($host);
$p->close();
$p = Net::Ping->new("icmp");
$p->bind($10.100.91.1); # Specify source interface of pings
foreach $host (@host_array)
{
print "$host is ";
print "NOT " unless $p->ping($host, 2);
print "reachable.\n";
sleep(1);
}
$p->close();
$p = Net::Ping->new("tcp", 2);
# Try connecting to the www port instead of the echo port
$p->port_number(getservbyname("http", "tcp"));
while ($stop_time > time())
{
print "$host not reachable ", scalar(localtime()), "\n"
unless $p->ping($host);
sleep(300);
}
undef($p);
# Like tcp protocol, but with many hosts
$p = Net::Ping->new("syn");
$p->port_number(getservbyname("http", "tcp"));
foreach $host (@host_array) {
$p->ping($host);
}
while (($host,$rtt,$ip) = $p->ack) {
print "HOST: $host [$ip] ACKed in $rtt seconds.\n";
}
# High precision syntax (requires Time::HiRes)
$p = Net::Ping->new();
$p->hires();
($ret, $duration, $ip) = $p->ping($host, 5.5);
printf("$host [ip: $ip] is alive (packet return time: %.2f ms)\n", 1000 * $duration)
if $ret;
$p->close();
# For backward compatibility
print "$host is alive.\n" if pingecho($host);
