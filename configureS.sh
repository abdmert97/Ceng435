r3=$(getent ahosts "r3" | cut -d " " -f 1 | uniq)

r3_adapter=$(ip route get $r3 | grep -Po '(?<=(dev )).*(?= src| proto)')


sudo tc qdisc add dev $r3_adapter root netem delay 40ms 10ms distribution normal
