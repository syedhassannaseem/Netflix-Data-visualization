import pandas as pd
import matplotlib.pyplot as plt

#read csv file
df = pd.read_csv("netflix/netflix_titles.csv")
#data cleaning

df.drop_duplicates(inplace=True)
df.sort_values(by=["show_id","type","title","director","cast","country","date_added","release_year","rating","duration","listed_in","description"],ascending=True,inplace=True)


#Number of Movies and Tv Shows

total = df["type"].value_counts()
plt.bar(total.index,total.values,color="purple",label="No of Movies")
plt.title("Numbers of Movies vs Tv Show in Netflx",fontweight='bold',fontsize=16)
plt.xlabel("Types",fontweight='light',fontsize=12)
plt.ylabel("Numbers of Movies and Tv Show",fontweight='light',fontsize=12)
plt.legend()
plt.savefig("netflix/bar.png",dpi = 300 , bbox_inches = "tight")
plt.show()

# percentage rating of contant

total=df["rating"].value_counts()
plt.figure(figsize=(10, 8))
plt.pie(total.values,labels=total.index  , autopct="%1.1f%%")
plt.legend(loc='center left', bbox_to_anchor=(1,0.6))
plt.title("Rating of Contant",fontweight='bold',fontsize=16)
plt.savefig("netflix/pie.png",dpi = 300 , bbox_inches = "tight")
plt.show()

#release Movie per years

total = df["release_year"].value_counts()
plt.plot(total.index , total.values , color = "c",marker = "d",linestyle = "--", linewidth = 0.5 , label = "Numbers of  Movies realease in years")
plt.legend()
plt.title("Release Movies per Year",fontweight='bold',fontsize=16)
plt.xlabel("Total Movies",fontweight='light',fontsize=12)
plt.ylabel("Years",fontweight='light',fontsize=12)
plt.grid()
plt.savefig("netflix/plot.png",dpi = 300 , bbox_inches = "tight")
plt.show()

# Distritution of movies Duration

df = df.dropna(subset=['duration'])
total = df[df["type"] == 'Movie'].copy()
total["duration_int"] = total["duration"].str.replace(" min", "").astype(int)

plt.hist(total["duration_int"],color="orange",edgecolor='black',bins=30,label="Total Movie Duration")
plt.legend()
plt.xlabel("Total Numbers of Movies",fontweight='light',fontsize=12)
plt.title("Distribution of Movies Duration",fontweight='bold',fontsize=16)
plt.savefig("netflix/hist.png",dpi = 300 , bbox_inches = "tight")
plt.show()

# Top 10 Countries with the highest Number of Shows

total = df["country"].value_counts().head(10)
plt.barh(total.index,total.values,color=["brown"],label="Highest Number of Tv show")
plt.xlabel("Total umbers of TV shows",fontweight="light",fontsize=12)
plt.ylabel("Contries Name",fontweight="light",fontsize=12)
plt.title("Top 10 Contries with highest number of Tv Shows",fontweight="bold",fontsize=16)
plt.legend()
plt.tight_layout()
plt.savefig("netflix/barh.png",dpi = 300 , bbox_inches = "tight")
plt.show()

# compare of Movies and Tv show release per year
total= df.groupby(["release_year","type"]).size().unstack().fillna(0)
fig , ax = plt.subplots(1,2,figsize=(12,5))

ax[0].bar(total.index,total["Movie"],color="orange")
ax[0].set_title("Total number of Movies release per Year",fontsize = 13 , fontweight="bold")
ax[0].set_xlabel("Years",fontweight="light",fontsize=12)
ax[0].set_ylabel("Numbers of Movies" , fontsize = 12 , fontweight= "light")
fig.suptitle("comparition of Movies and Tv show release per year",fontweight = "heavy" ,fontsize = 17)
plt.grid()

ax[1].bar(total.index,total["TV Show"],color="green")
ax[1].set_title("Total number of TV shows release per Year",fontsize = 13 , fontweight="bold")
ax[1].set_xlabel("Years",fontweight="light",fontsize=12)
ax[1].set_ylabel("Numbers of TV shows" , fontsize = 12 , fontweight= "light")
plt.tight_layout()
plt.grid()
plt.savefig("netflix/subplots.png",dpi = 300 , bbox_inches = "tight")
plt.show()


