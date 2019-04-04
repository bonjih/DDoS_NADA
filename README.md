# DDoS_NADA
Solving a real world problem

For a couple of days starting February 19 2019, a network experienced a Distributed Denial-of-Service attack (DDoS) on its Fortigate 600D 
firewall. The DDOS attack took the form of multiple log in attempts per second which forced the Fortigate’s CPU to reach and stay at 100%.
The Fortigate’s CPU being at 100% prevented the Fortigate to perform other actions and therefore packets were dropped. 

All internal generated traffic could not access the internet / external services.

The objective of this project is to create a novel detection and prediction method against DDoS attacks by using chaotic and traffic analysis on real-time traffic at the firewall. To meet the objective, a combination of well-known and implemented techniques are used. The outcome of the techniques will result in a Network Anomaly Detection Algorithm (NADA) for DDOS prediction.

This DDoS Detection Algorithm is based on Pre-processing of the network traffic and then find a predicted method using Chaos Theory and Neural Network as detail in Yonghong 2013 and Chonka et al. 2009, and many other works. 

Chaos Theory assumes that ‘normal’ traffic patterns are chaotic in nature, therefore abnormal traffic patterns are non-chaotic. Normally, when traffic trends toward a non-chaotic state i.e. traffic goes exponential, a DDoS attacked is said to be imminent. In our case, and when the DDoS attack was underway, it was observed that the traffic did not trend up as expected, i.e. the traffic did not transition from a normal chaotic state to a none chaotic state with exponential traffic. 





Due to this fact, and the traffic shape being sinusoidal in form and the traffic shape being ‘similar’ in form over a monthly average, a Fast Fourier Transform (FFT) is used to represent the time-dependent incoming signal, then compute its amplitude and period (determine the parodic function as y=f(t) - ( T=2π and freq=1/2π H). These forms are then learnt and stored as typical traffic patterns using Machine Learning. Additionally, the traffic patterns of the DDoS attack are feed through a FFT for analysis. Figure 4 shows the COGC DDoS period in the red square
