# Ceng435
Term Project
kill process at port : sudo kill -9 $(sudo lsof -t -i:30211)


the costs of the links (s-r1, r1-d) will be estimated and saved by r1,  the costs of the links (s-r3, r3-d) will be estimated and saved by r3, and finally, the costs of the links (s-r2,r1-r2, r2-r3, r2-d) will be estimated and saved by r2

s sadece verici ve r1, r2, r3 e veriyor
d sadece alıcı ve r1,r2,r3ten alıyor
diğerleri hem alıcı hem verici
r1 sden alıyor r2 ile dye veriyor
r2 s,r1den alıyor d,r3e veriyor
r3 s,r2den alıyor d ye veriyor
