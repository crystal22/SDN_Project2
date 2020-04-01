**Problem Statement** 

Optimizing wireless networks in real-time is a very challenging task. Successful models have recently relied on machine learning techniques to predict users behaviors, thus resource allocation can be done in advance. The goal of this project is to propose and implement machine learning (ML) algorithms to analyze data collected from a WiFi access point (AP), and then to identify which type(s) of applications are running on this network, as well as the mobility of users. Dataset for this project will be collected from a physical AP. Typical applications running on the AP would be: video streaming, HTTP web, FTP downloading, P2P downloading, and email. Key fields in the dataset include traffic throughput, transmission and reception rates, and signal power.

**Project Justification**

Wireless networks are key enablers of ubiquitous communication which particularly requires enhanced quality of user experience(QoE) at optimized rate with optimum resource utilization. Accurate predictions on user behaviors provides an in-depth understanding on the dynamics of network usage, which is essential in the advance management of network activities, such as capacity planning and provisioning, and therefore can efficiently facilitate network optimization and improve application performance. Using machine learning techniques in WiFi networks enables these networks to predict and adapt to changing environments promptly while continue learning about their environments.
This project will apply ML techniques on user activity recognition and prediction in a wireless network, with great significance in helping wireless networks making timely decisions on resource distribution to meet all levels of user demands.

**Project Objectives** 

1. To extend our understanding of WiFi technologies, WiFi user behaviorand WiFi network performance.
2. To characterize user behavior in terms of application mix and mobility based on the data collected from a WiFi AP.
3. To build parametrized models for identifying application type and user mobility using ML techniques.
4. To apply our study further on WiFi user behaviour prediction and resourceallocation.
    
**Related Work** 

• **Application of Machine-Learning Based Prediction Techniques in Wireless Networks**[Bhu14]: the authors provide a survey on various problems of wireless networks that have been solved using machine-learning based prediction techniques and identify additional problems towhich prediction can be applied. They present some gaps in the researchdone in this area till date.

• **Wireless Network Traffic Disaggregation using Bayesian Non-parametric Techniques**[For+18]: this paper presents a machine learn-ing spectrum awareness framework capable of characterizing and inferringthe application layer protocol states of multiple interleaved wireless net-work traffic flows using only externally observable energy detector features.

• **Application of Machine Learning in Wireless Networks: KeyTechniques and Open Issues**[Sun+19]: this paper details the recentadvances of the applications of ML in wireless communication.

• **Characterizing user behavior and network performance in a public wireless LAN**[Bal+02]: using a workload captured at a well-attended ACM conference, the authors present and analyze user behaviorand network performance in a public-area wireless network.

• **Modeling User Activity Patterns for Next-Place Prediction**[Yu+15]: the authors propose to infer the individual’s next activity by modeling useractivity patterns, and then predict the next location of the user on thebasis of the inferred next activity.

**Activity Plan**

1.  **Feb 2020** : Literature review study on WiFi network user behavior [Bal+02]and ML application in WiFi network [For+18], including key techniques[Bhu14]and prediction approaches[Sun+19].
2.  **March 2020** : Coding, Implementation & Experiments.Data preparation. We propose to observe the data flows in two ways: single traffic flow and multiple traffic flow. Data extraction will be doneas per single user/device and as per a collection of users connected to oneAP from raw data. ML techniques implementation. 
    
    • **Scenario 1**: For identification of application types, we propose to explore unsupervised learning approach to spectrum sensing where knowledge ofthe user protocol (user application) at the application layers is discovered from simple energy detector features. Inspired by [For+18],We propose to investigate on Bayesian Nonparametric Techniquesto automatically characterize and infer the application layer state ofuser traffic using some energy detector features. These features will be derived from characteristics of RF transmis-sions that can be extracted from measurements, energy detection: such as transmission duration, time of arrival, center frequency, band-width, traffic throughput, transmission and reception rates, and sig-nal power.The plan of our study will incorporated an unsupervised Bayesian nonparametric HMM model training procedure, introducing a pow-erful capability to discover and characterize latent primary user pro-tocol states from observable data, together with efficient HMM re-cursions for protocol classification, state recognition and anomaly detection. For single isolated traffic flows, we will used a Bayesian nonparamet-ric technique to construct hidden Markov model (HMM) representa-tions of specific protocols.  The learned HMM models, with hidden states closely corresponding to actual protocol states, will be use forprotocol classification and state recognition given a stream of energydetector observables from an isolated traffic flow.For various traffic, various single protocol HMMs could be combineinto a factorial hidden Markov model (FHMM) representing multipleheterogeneous  interleaved  flows. We will use the FHMM to inferthe states of the interleaved flows directly from observations of theaggregate traffic.
    
    • **Scenario 2**: For identification of application types, unsupervised ML will be ap-plied, clusters will be defined as plotting of transmission rate and throughput for each user. For user mobility, we consider transmissionpower and signal strength to be the main indicators on user distancefrom an AP. We define user mobility as user connection status andsignal strength, and anticipate to predict distances of the user fromthe AP when using different types of application.  Next-location pre-diction can be discussed depending on the progress of experiments.Extra experiments may be needed to prove how keywords set affectsthe final output.Tests  on  ML  Algorithms.   For  testing,  we  will  compare  plotting  oftransmission rate and throughput of predicted application type and thesame type of application running on our own device, likewise, relationshipbetween signal strength and distance from the AP will be tested manuallyon our own devices.Evaluate and perform the model.
 
3.  **March 2020** : Simulation and demo. We  will  present  an  experimental demonstration on an emulated WiFi LAN comprising multiple flows carry-ing different application layer traffic types (video streaming, HTTP web,FTP downloading, P2P downloading, and email).Network environment configurationMonitoring and evaluation(to be decided during experiments).
4.  **April 2020** :  Final report

**References**

[Bal+02]Anand Balachandran et al. “Characterizing user behavior and net-work performance in a public wireless LAN”. In: Proceedings of the2002 ACM SIGMETRICS international conference on Measurementand modeling of computer systems. 2002, pp. 195–205.

[Bhu14]Gitanjali  Bhutani. “Application of machine-learning based prediction techniques in wireless networks”.  In: Int’l J. of Communications, Network and System Sciences2014 (2014).

[Yu+15]Chen Yu et al. “Modeling user activity patterns for next-place prediction”. In: IEEE Systems Journal11.2 (2015), pp. 1060–1071.

[For+18]Gabriel Ford et al. “Wireless network traffic disaggregation using Bayesian nonparametric techniques”. In: 2018 52nd Annual Conference on Information Sciences and Systems (CISS). IEEE. 2018,pp. 1–6.

[Sun+19]Yaohua Sun et al. “Application of machine learning in wireless net-works: Key techniques and open issues”. In:IEEE CommunicationsSurveys & Tutorials21.4 (2019), pp. 3072–310
