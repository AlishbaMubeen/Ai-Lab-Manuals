
import skfuzzy as fuzz
# Applying FCM
# cntr (centers), u (membership matrix), fpc (Fuzzy Partition Coefficient)
cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(
 data.T, c=3, m=2, error=0.005, maxiter=1000)
print(f"The Fuzzy Partition Coefficient (FPC) is: {fpc:.4f}")

!pip install skfuzzy

import skfuzzy as fuzz
# Applying FCM
# cntr (centers), u (membership matrix), fpc (Fuzzy Partition Coefficient)
cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(
 data.T, c=3, m=2, error=0.005, maxiter=1000)
print(f"The Fuzzy Partition Coefficient (FPC) is: {fpc:.4f}")
