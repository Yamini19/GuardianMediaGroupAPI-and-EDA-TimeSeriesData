import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read data from the CSV file
df = pd.read_csv("results.csv")

# Create a new dataframe by grouping dates
df['webPublicationDate']=pd.to_datetime(df['webPublicationDate'])
df["Date"]=  df['webPublicationDate'].dt.strftime('%Y-%m-%d')
df_Date= pd.DataFrame({'Articles' : df.groupby( ["Date"] ).size()}).reset_index()

print(df_Date)

# Average number of articles
print(df_Date["Articles"].mean())
# Create new dataframe by grouping Section Names
df_Section= pd.DataFrame({'Articles' : df.groupby(["sectionName"]).size()}).reset_index()
# sorting
df_Section.sort_values("Articles", ascending= False)

# Plot number of articles with respect to different sections
sns.set_theme(style="whitegrid")
plt.figure(figsize=(25, 10))
plt.xticks(rotation=90)
ax = sns.barplot(x="sectionName", y="Articles", data=df_Section)
plt.xlabel('Section Name', fontsize=25)
plt.ylabel('Number of Articles', fontsize=25)
plt.title("Number of Articles vs Sections",fontsize=40)
ax.tick_params(axis='both', which='major', labelsize=18)
ax.tick_params(axis='both', which='minor', labelsize=20)
plt.savefig("Section.jpeg", bbox_inches="tight")

# Add Year and month columns to the previous Dataframe (grouped by Date)
df_Date["Year"]= pd.DatetimeIndex(df_Date['Date']).year
df_Date["Month"]= pd.DatetimeIndex(df_Date['Date']).month

df_Date["Date"]= pd.to_datetime(df_Date["Date"])
df_Date= df_Date.set_index('Date')
df_Date["WeekDay_Name"] = df_Date.index.day_name()

# Visualize time series Data
sns.set(rc={'figure.figsize':(30, 10)})
ax=df_Date['Articles'].plot(linewidth=1);
plt.title("Time Series - Number of Articles",fontsize=30)
plt.ylabel("Number of Articles", fontsize=22)
plt.xlabel("Timeline", fontsize=22)
ax.tick_params(axis='both', which='major', labelsize=16)
ax.tick_params(axis='both', which='minor', labelsize=16)
plt.savefig("TimeSeries.jpeg")