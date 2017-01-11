import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
pixar=pd.read_csv("C:/Users/hp/Downloads/PixarMovies.csv")
pixar.head()
#cleaning data removing % and making score u of 100 for imdb
pixar['Domestic %']=pixar['Domestic %'].str.rstrip('%').astype('float')
pixar['International %']=pixar['International %'].str.rstrip('%').astype('float')
pixar['IMDB Score']=pixar['IMDB Score']*10
# Adding new features
pixar['Profit']=pixar['Worldwide Gross']-pixar['Production Budget'] 
pixar['Domestic Profit']=pixar['Domestic Gross']-pixar['Production Budget']
pixar['International Profit']=pixar['Profit']-pixar['Domestic Profit']
pixar.dtypes
# settng movie as index column
pixar.set_index('Movie',inplace=True)
# now analysisng critics score
critics_review=pixar[['RT Score','IMDB Score','Metacritic Score']]
critics_review.plot(figsize=(10,6),grid=False,linewidth=2)
plt.title("Critics Review")
plt.show()
#analysing through boxplot
critics_review.boxplot(figsize=(9,5),grid=False)
plt.title("Critics Review")
plt.show()
#Comparing International Profit vs Domestic Profit
pixar.sort_values('Profit')[['Profit','International Profit','Domestic Profit']].plot(kind='bar',figsize=(15,6),grid=False)
plt.title("Comparing International Profit vs Domestic Profit")
plt.show()
#Comparing Production Budget vs Opening Weekend Collection
op=pixar[['Opening Weekend','Production Budget']]
op.sort_values('Opening Weekend').plot(kind='bar',figsize=(15,6),grid=False)
plt.title("Comparing Production Budget vs Opening Weekend Collection")
plt.show()
# comparing domestic vs international collection
pixar[['Domestic %','International %']].sort_values('International %').plot(kind='bar',figsize=(15,6),stacked=True,grid=False)
plt.title("Domestic collection vs International collection in %")
plt.show()
# how pixar took up the  international market  
pixar_year=pixar.set_index("Year Released")
pixar_year[['Domestic %','International %']].plot(kind='bar',figsize=(15,6),grid=False)
plt.title("Comparing Domestic market vs International market year on year")
plt.show()
#The big stage: Oscars
pixar[['Oscars Nominated','Oscars Won']].plot(kind='bar',figsize=(15,6),grid=False)
plt.title("The big stage: Oscars")
plt.show()
