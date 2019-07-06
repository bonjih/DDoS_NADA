# DDoS_NADA
Solving a real world problem

For a couple of days starting February 19 2019, a network experienced a Distributed Denial-of-Service attack (DDoS) on its Fortigate 600D 
firewall. The DDoS attack took the form of multiple log in attempts per second which forced the Fortigate’s CPU to reach and stay at 100%.
The Fortigate’s CPU being at 100% prevented the Fortigate to perform other actions and therefore packets were dropped. 

All internal generated traffic could not access the internet / external services.

![Capture](https://user-images.githubusercontent.com/37001472/56445038-9dea2200-633e-11e9-91c5-7fec3b8fd77c.PNG)

                              Figure 1 – DDoS via multiple login and fail attempts

The objective of this project is to create a novel detection and prediction method against DDoS attacks by using chaotic and traffic analysis on real-time traffic at the firewall. To meet the objective, a combination of well-known and implemented techniques are used, which includes Fast Fourier Transform (FFT). The outcome of the techniques will result in a Network Anomaly Detection Algorithm (NADA) for DDoS prediction.

Chaos Theory for DDoS assumes that ‘normal’ traffic patterns are chaotic in nature, therefore abnormal traffic patterns are non-chaotic (Yonghong 2013 and Chonka et al. 2009). Normally, when traffic trends toward a non-chaotic state the traffic goes exponential, a DDoS attacked is said to be imminent. In our case, and when the DDoS attack was underway, it was observed that the traffic did not trend to exponential. Traffic decreased (figure 2). Due to this fact, and the traffic shape being sinusoidal in form and the traffic shape being ‘similar’ in form over a monthly average, a Fast Fourier Transform (FFT) is used to represent the time-dependent incoming signal. A computation is made on its period (determine the parodic function as y=f(t) - ( T=2π and freq=1/2π H). These forms are then learnt and stored as typical traffic patterns. 

This DDoS Detection Algorithm is based on Pre-processing FFT of network traffic as desciibed in 'Fouladi, RF, Kayatas, CE, Anarim, E, 2018, Statistical Measures: Promising Features for Time Series Based DDoS Attack Detection'. The principle idea used is that the distribution of energy in different frequencies [from FTT] is revealed by PSD. Since period and frequency are the reverse of each other, dominant periods can be identified by finding frequencies which carry most of the energy. Therefore, it is this variance (feature) between the energy in a ‘normal’ traffic pattern and DDoS traffic pattern used to detection and make DDoS prediction.





![Figure_4](https://user-images.githubusercontent.com/37001472/55590827-57f66100-5777-11e9-93f3-6e17d1bdf0a1.png)

                            Figure 2 – Firewall external traffic shape over 1 week
                            

![Capture](https://user-images.githubusercontent.com/37001472/55590492-66904880-5776-11e9-8e01-7ca622d97589.PNG)

                         Figure 3 – DDoS attack profile, high traffic period should be in the middle



