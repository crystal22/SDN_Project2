import warnings
warnings.filterwarnings('ignore')
#pip install bayesian-hmm
import bayesian_hmm

import matplotlib.pyplot as plt
# create emission sequences
base_sequence = list(range(5)) + list(range(5, 0, -1))
sequences = [base_sequence * 20 for _ in range(50)]

fig, ax = plt.subplots()
min_val, max_val = 0, 5
ax.matshow(sequences, cmap=plt.cm.Blues)

#test with web_mac2 dlthrough put
#base_sequence =[197040,0,0,0,20544,147896,172208,277664,161104,16424,277696,380968,1979264,487384,38688,2189080,618656,323920,336328,639280,1835944,325296,111608,284528,289568,284032,137176,577376,932496,5136,8616,68624,58560,48048,5424,6152,69960]
#sequences = [str(i) for i in base_sequence]

# initialise object with overestimate of true number of latent states
hmm = bayesian_hmm.HDPHMM(sequences, sticky=False)
hmm.initialise(k=20)

results = hmm.mcmc(n=500, burn_in=100, ncores=3, save_every=10, verbose=True)

# print final probability estimates (expect 10 latent states)
hmm.print_probabilities()



