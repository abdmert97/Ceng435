# Ceng435
Term Project

*Installation*
---
## Discovery Part:
  1. Create the network topology and transfer the related python scripts to the nodes. Every node has its own script and its related scripts are named as nameofthenode+".py". For the discovery part the scripts are under the "discovery" folder.
  2. Run the scripts. All scripts should be run together to obtain a successful result. 
  ```
      $ python s.py
  ```  
  3. The result files will be on the nodes r1,r2,r3 and will be named "link_costs.txt".

## Experiment Part:
  For this part, only the nodes s, r3, d are used because the shortest path contains only these nodes.
  1. Create the network topology and transfer the related python scripts to the nodes. Every node has its own script and its related scripts are named as nameofthenode+".py". For the discovery part the scripts are under the "discovery" folder.
  2. Transfer the related configuration scripts to the nodes. Every node has its own script and its related scripts are named as "configure"+nameofthenode(capital)+".sh"
  3. Synchronize nodes using ntp
   ```
      $ sudo ntpdate pool.ntp.org
  ```
  4. Configure the node with the bash script for the node. Bash script takes the network emulation delay as argument. 
  Example for configuration of R3 node with 40ms+-5ms delay
  ```
      $ ./configurationR3.sh 40 10
  ```
  5. Run the scripts. All scripts should be run together to obtain a successful result.
  ```
      $ python s.py
  ```  
port 30(server)(client)0
