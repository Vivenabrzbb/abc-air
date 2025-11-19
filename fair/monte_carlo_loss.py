# Run the above model and save exceedance curve
import matplotlib.pyplot as plt
from fair_model import annual_loss
df = pd.Series(annual_loss).sort_values(ascending=False).reset_index(drop=True)
df.plot(logy=True, title="Loss Exceedance Curve – ABC Air (R-001)")
plt.xlabel("Rank")
plt.ylabel("Annual Loss (£)")
plt.savefig("reports/loss_exceedance.png", dpi=300)