import pandas as pd
bNames = ["noah", "liam", "jacob", "william", "mason", "ethan", "michael", "alexander", "james", "elijah"]
gNames = ["emma", "olivia", "sophia", "isabella", "ava", "mia", "abigail", "emily", "charlotte", "madison"]
bFreq = [183330, 173981, 163266, 159945, 145677, 134687, 122222, 111111, 100000, 2]
gFreq = [183329, 173980, 163265, 159944, 145676, 134686, 122221, 111110, 99999, 1]
df = pd.DataFrame({
    'bNames':bNames, 
    'bFreq:':bFreq, 
    'gNames':gNames,
    "gFreq:":gFreq
    })
print(df)
dfDescribe = round(df.describe())
print(dfDescribe)