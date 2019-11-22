#!/bin/bash
s=$(getent ahosts "s" | cut -d " " -f 1 | uniq)
d=$(getent ahosts "d" | cut -d " " -f 1 | uniq)

s_adapter=$(ip route get $s | grep -Po '(?<=(dev )).*(?= src| proto)')
d_adapter=$(ip route get $d | grep -Po '(?<=(dev )).*(?= src| proto)')


sudo tc qdisc replace dev $s_adapter root netem delay $1ms $2ms distribution normal
sudo tc qdisc replace dev $d_adapter root netem delay $1ms $2ms distribution normal
