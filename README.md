<!--2171999 - Ramazan Selim Şahin-->
<!--2171981 - Abdurrahman Mert Şafak-->
# Ceng435
### This readme file includes the installation & run instrucions of Ceng435 Term Project Part 1

*How To Run*
---
## Discovery Part:
  1. Create the network topology and transfer the related python scripts to the nodes. Every node has its own script and its related scripts are named as nameofthenode+".py". For the discovery part the scripts are under the "discoveryScripts" folder.
  2. Run the scripts. All scripts should be run together to obtain a successful result. Run the scripts in the order: s and d first, r1 and r3 second and r2 last.
  ```
      $ python s.py
  ```  
  3. The result files will be on the nodes r1,r2,r3 and will be named "link_costs.txt".

## Experiment Part:
  For this part, only the nodes s, r3, d are used because the shortest path contains only these nodes.
  1. Create the network topology and transfer the related python scripts to the nodes. Every node has its own script and its related scripts are named as nameofthenode+".py". For the discovery part the scripts are under the "experimentScripts" folder.
  2. Transfer the related configuration scripts to the nodes. Every node has its own script and its related scripts are named as "configure"+nameofthenode(capital)+".sh"
  3. Synchronize nodes using ntp
   ```
      $ sudo ntpdate pool.ntp.org
  ```
  4. Configure the node with the bash script for the node.TC is used with "replace" argument in this script, you should use it with "add" in first execution. Bash script takes the network emulation delay as argument. 
  Example for configuration of R3 node with 40ms+-5ms delay
  ```
      $ ./configurationR3.sh 40 10
  ```
  5. Run the scripts. All scripts should be run together to obtain a successful result. Run the scripts in the order: d first, r3 second and s last.
  ```
      $ python r3.py
  ``` 
  6. The result files will be on the node d and will be named "end_to_end.txt".

*Info*
---
  * The local ports are choosen with the pattern: 
    * 0 is the code for "s" node
    * 1 is the code for "r1" node
    * 2 is the code for "r2" node
    * 3 is the code for "r3" node
    * 4 is the code for "d" node
    * 30+(server node)+(client node)+0
  E.g. when "s" is server and "r3" is client, selected port is 30030
  
  * link_costs.txt: 
    * Every message's rtt is recorded. The format is "connectionnumber"->"message number" - "rtt"
    * Every link's average cost is recorded at the end of the line. The format is "connectionnumber" - "average rtt"
    
  * end_to_end.txt: 
    * Every message's end to end delay is recorded.
    * Average is recorded at the end of the line.    
