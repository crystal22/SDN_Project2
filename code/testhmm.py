import numpy as np
import matplotlib.pyplot as plt
from hmmlearn import hmm

# Build an HMM instance and set parameters
model = hmm.GMMHMM(n_components=5,n_mix=1, covariance_type="full")
#test with web_mac2 dlthrough put
base_seq =[197040,0,0,0,20544,147896,172208,277664,161104,16424,277696,380968,1979264,487384,38688,2189080,618656,323920,336328,639280,1835944,325296,111608,284528,289568,284032,137176,577376,932496,5136,8616,68624,58560,48048,5424,6152,69960]
plt.plot(base_seq)


seq = np.array(base_seq).reshape(-1, 1)
tr = model.fit(seq)
re = model.predict(seq)
X, Z = model.sample(len(base_seq))
px = [i[0] for i in X]

plt.plot(px)
plt.show()
"""
startprob = np.array([0.964,0.036])
# The transition matrix, note that there are no transitions possible between component 1 and 3
transmat = np.array([[0.084, 0.916],
                     [1.0, 0.0]])

# The means of each component
means = np.array([[16424, 2189080],[0, 69960]])

# The covariance of each component
covars = .5 * np.tile(np.identity(2), (2, 1, 1))

# Build an HMM instance and set parameters
model = hmm.GMMHMM(n_components=2,n_mix=2, covariance_type="full")

# Instead of fitting it from the data, we directly set the estimated parameters, the means and covariance of the components
model.startprob_ = startprob
model.transmat_ = transmat
model.means_ = means
model.covars_ = covars

# Generate samples
X, Z = model.sample(100)
print()
# Plot the sampled data
plt.plot(X[:, 0], X[:, 1], ".-", label="observations", ms=6, mfc="orange", alpha=0.7)

# Indicate the component numbers
for i, m in enumerate(means):
    plt.text(m[0], m[1], 'Component %i' % (i + 1),
             size=17, horizontalalignment='center',
             bbox=dict(alpha=.7, facecolor='w'))

plt.legend(loc='best')
plt.show()
"""