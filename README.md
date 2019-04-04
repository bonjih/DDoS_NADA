# DDoS_NADA
Solving a real world problem

For a couple of days starting February 19 2019, a network experienced a Distributed Denial-of-Service attack (DDoS) on its Fortigate 600D 
firewall. The DDOS attack took the form of multiple log in attempts per second which forced the Fortigate’s CPU to reach and stay at 100%.
The Fortigate’s CPU being at 100% prevented the Fortigate to perform other actions and therefore packets were dropped. 

All internal generated traffic could not access the internet / external services.

