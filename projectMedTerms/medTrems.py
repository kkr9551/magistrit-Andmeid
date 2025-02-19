import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;

#read csv
PairMedTerms = pd.read_csv("./database/MedTermPairFreq.csv", sep=";")

total_tokens = 579543713
million = 1000000

#calculate relative frequency of both estonian and foreign terms, 
# the value is in the pattern: x per million.
PairMedTerms["rel_Freq_Est"] = round(
    PairMedTerms["EcountINsample2"] / (total_tokens) * million, 3
)
PairMedTerms["rel_Freq_Fore"] = round(
    PairMedTerms["FcountINsample2"] / (total_tokens) * million, 3
)

# move the column to the proper place
temp_col = PairMedTerms.pop("rel_Freq_Est")
PairMedTerms.insert(5, temp_col.name, temp_col)

sec_temp_col = PairMedTerms.pop("rel_Freq_Fore")
PairMedTerms.insert(8, sec_temp_col.name, sec_temp_col)
#print(PairMedTerms.info())

#PairMedTerms.to_csv("./database/newPairMedTerms.csv", index=False)

# break the dataframe into two sub-dataframes: 
# dominant estonian word and dominant foreign word
EstDom = PairMedTerms.loc[
    PairMedTerms["EcountINsample2"] >= PairMedTerms["FcountINsample2"]
].reset_index(drop=True)
ForeDom = PairMedTerms.loc[
    PairMedTerms["EcountINsample2"] < PairMedTerms["FcountINsample2"]
].reset_index(drop=True)

# rank the sub-dataframe in an ascending order according to relative frequency 
EstDom["ranked"] = EstDom["rel_Freq_Est"].rank(ascending=1)
EstDom = EstDom.set_index("ranked").sort_index().reset_index(drop=True)
EstDom["fore_Ratio"] = round(
    EstDom["FcountINsample2"] / EstDom["EcountINsample2"], 3
)

# Take the median and select part of sub-dataframe whose relative frequency is above median
sub_EstDom = EstDom.loc[EstDom["rel_Freq_Est"] >= EstDom.at[31, "rel_Freq_Est"]]

# rank the sub-dataframe in an ascending order according to relative frequency
ForeDom["ranked"] = ForeDom["rel_Freq_Fore"].rank(ascending=1)
ForeDom = ForeDom.set_index("ranked").sort_index().reset_index(drop=True)

ForeDom["est_Ratio"] = round(
    1 - (ForeDom["EcountINsample2"] / ForeDom["FcountINsample2"]), 3
)


'''
ForeDom["fore_Ratio"] = round(
    ForeDom["FcountINsample2"] / ForeDom["EcountINsample2"], 3
)
'''

# Take the median and select part of sub-dataframe whose relative frequency is above median
sub_ForeDom = ForeDom.loc[ForeDom["rel_Freq_Fore"] >= ForeDom.at[38, "rel_Freq_Fore"]]
#sub_ForeDom.to_csv("./database/sub_ForeDom.csv", index=False)

#print(sub_EstDom.info())
#print(sub_ForeDom.info())

'''
newSampledFrame = pd.concat([sub_EstDom, sub_ForeDom])
newSampledFrame.to_csv("./database/new_SampledFrame.csv", index=False)
'''

#sub_EstDom.to_csv("./database/sub_EstDom.csv", index=False)

#plot a histogram with two sectored sub-dataframes

plt.hist(
    sub_EstDom["fore_Ratio"], 
    bins=40, 
    label="Dominant estonian words", 
    edgecolor="black",
    color="blue",
    alpha=0.8
)

plt.hist(
    sub_ForeDom["est_Ratio"],
    bins=40, 
    label="Dominant foreign words",
    edgecolor="grey",
    color="orange",
    alpha=0.7
)


plt.xlabel("Ratio")
plt.ylabel("Frequency")
plt.legend()
plt.show()



#get a list of column names in this df
#columnNames = PairMedTerms.columns
#print(columnNames)

#a = PairMedTerms[PairMedTerms["EnglishTerms"] == "euthanasia"]
#print(a)
#the basic dataframe constructor is DF[data, index, column]

#ratio_Est_vs_Fore = (newFra_1["countINsample2"].sum()) / (newFra_1["countINsample2.1"].sum())
#ratio_Fore_vs_Est = (newFra_2["countINsample2.1"].sum()) / (newFra_2["countINsample2"].sum())

'''
newFra_1["ranked"] = newFra_1["countINsample2"].rank(ascending=1)
newFra_1 = newFra_1.set_index("ranked").sort_index().reset_index(drop=True)
newFra_1["Estonian_vs_foreign"] = round(newFra_1["countINsample2"] / newFra_1["countINsample2.1"], 2)
newFra_1["rel_Freq_Est"] = round(newFra_1["countINsample2"] / (newFra_1["countINsample2"].sum()), 4)
newFra_1["rel_Freq_Fore"] = round(newFra_1["countINsample2.1"] / (newFra_1["countINsample2.1"].sum()), 4)
'''

#newFra_1["Score"] = round((newFra_1["countINsample2"] / newFra_1["countINsample2.1"]) / ratio_Est_vs_Fore, 2)

#newFra_1["ranked"] = newFra_1["Estonian_vs_foreign"].rank(ascending=1)
#newFra_1 = newFra_1.set_index("ranked").sort_index().reset_index(drop=True)
#print(newFra_1)

#newFra_1.to_csv("./database/newFrame2.csv", index=False)

'''
newFra_2["ranked"] = newFra_2["countINsample2.1"].rank(ascending=1)
newFra_2 = newFra_2.set_index("ranked").sort_index().reset_index(drop=True)
newFra_2["foreign_vs_Estonian"] = round(newFra_2["countINsample2.1"] / newFra_2["countINsample2"], 2)
newFra_2["rel_Freq_Est"] = round(newFra_2["countINsample2"] / (newFra_2["countINsample2"].sum()), 4)
newFra_2["rel_Freq_Fore"] = round(newFra_2["countINsample2.1"] / (newFra_2["countINsample2.1"].sum()), 4)
print(newFra_2)
'''

#newFra_1.to_csv("./database/relFreqFrame.csv", index=False)

#newFra_2.to_csv("./database/relFreqFrame_Fore.csv", index=False)
















