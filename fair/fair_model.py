import numpy as np
import pandas as pd

# FAIR parameters for R-001 (Brute-force → admin compromise)
TEF = 10          # attempts/day
Vuln = 0.9        # no MFA
LEF = TEF * Vuln
LM  = 500_000     # GBP per event
simulations = 10_000
annual_loss = np.random.exponential(LEF * LM * 365, simulations)
print(f"95th percentile annual loss: £{np.percentile(annual_loss, 95):,.0f}")
