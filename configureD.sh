r3=$(getent ahosts "r3" | cut -d " " -f 1 | uniq)

r3_adapter=$(ip route get $r3 | grep -Po '(?<=(dev )).*(?= src| proto)')

sudo tc qdisc replace dev $r3_adapter root netem delay $1ms $2ms distribution normal
