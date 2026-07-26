import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel("data/Premier-League-Attackers-Data.xlsx")
data["NPG Score"]=data["Non Penalty Goals"]/data["Non Penalty Goals"].max()
data["Assist Score"]= data["Assists"]/data["Assists"].max()
data["G90 Score"]= data["Goals Per 90"]/data["Goals Per 90"].max()
data["A90 Score"]= data["Assists Per 90"]/data["Assists Per 90"].max()
data["Career Score"]=(data["NPG Score"]*0.60+data["Assist Score"]*0.40)
data["Efficiency Score"]=(data["G90 Score"]*0.6+data["A90 Score"]*0.40)
#data["Weighted Score 1"]=(data["Non Penalty Goals"]*0.24+data["Assists"]*0.16+data["Goals Per 90"]*36+data["Assists Per 90"]*24)
data["Balanced Score"]=(data["NPG Score"]*0.24+data["Assist Score"]*0.16+data["G90 Score"]*36+data["A90 Score"]*24)
comparison = data[["Player", "Career Score", "Efficiency Score", "Balanced Score" ]]
print(comparison.sort_values("Balanced Score",ascending=False).head(20))
plt.scatter(data["Career Score"], data["Efficiency Score"], alpha=0.4)

highlight_players = ["Alan Shearer", "Erling Haaland", "Thierry Henry", "Wayne Rooney"]

highlight = data[data["Player"].isin(highlight_players)]

plt.scatter(
    highlight["Career Score"],
    highlight["Efficiency Score"],
    s=100
)
for i, player in enumerate(data["Player"]):
    plt.annotate(
        player,
        (data["Career Score"].iloc[i], data["Efficiency Score"].iloc[i]),
        fontsize=10,
        xytext=(5,5),
        textcoords="offset points"
    )

plt.xlabel("Career Score")
plt.ylabel("Efficiency Score")

plt.plot([0,1], [0,1], linestyle="--")

plt.title("Premier League Attackers: Career vs Efficiency")
plt.savefig("images/career_vs_efficiency.png", bbox_inches="tight")
plt.show()

table_data = data.sort_values("Balanced Score", ascending=False)[[
    "Player",
    "Career Score",
    "Efficiency Score",
    "Balanced Score"
]].head(10)

fig, ax = plt.subplots(figsize=(10,5))

ax.axis("off")

table = ax.table(
    cellText=table_data.values,
    colLabels=table_data.columns,
    loc="center"
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1,2)

import os
print(os.getcwd())

plt.savefig("images/player_rankings.png", bbox_inches="tight")
plt.close()