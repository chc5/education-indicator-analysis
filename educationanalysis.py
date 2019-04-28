

# Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def plot_corr(df,size=10):
    '''Function plots a graphical correlation matrix for each pair of columns in the dataframe.

    Input:
        df: pandas DataFrame
        size: vertical and horizontal size of the plot'''

    corr = df.corr()
    fig, ax = plt.subplots(figsize=(size, size))
    ax.matshow(corr)
    plt.xticks(range(len(corr.columns)), corr.columns);
    plt.yticks(range(len(corr.columns)), corr.columns);
    
def get_country_names(inds_df) :
  return country_names = inds_df.country_name.unique()
  
def df_corr_country(df, country):
  ''' Returns a df properly formatted to find correlation of indicators within a country'''
  # drop ids etc., get only rows with country, transpose
  df_corr = inds_df.drop(df.columns[[0, 1, 3]], axis=1)[df.country_name == country].T
  # fix columns
  df_corr.columns = df_corr.iloc[0]
  # drop first two rops
  df_corr = df_corr[2:]
  # df_corr = inds_df.drop(inds_df.columns[[0, 1, 3]], axis=1).drop(inds_df.columns[range(5,32)], axis=1)[inds_df.country_name == "Albania"]
  df_corr = df_corr.apply(pd.to_numeric)
  return df_corr

def plot_corr_by_country(inds_df, country):
  # change threshold to get more columns 
  df_corr = df_corr_country(inds_df, country)
  plot_corr(df_corr, size=20)
  
def get_xy_lists(xkey, ykey, inds_df):
  ''' Returns a 2d list a[0] and a[1] of x and y values for scatter plot specified with xkey and ykey in indf_df'''
  comparematrix = [[],[]]
  print(comparematrix)
  for i in country_names :
    df_corr = plot_corr_country(inds_df, i)
    if xkey in df_corr :
      for yearnum in range(2015, 2016):
        year = str(yearnum)
        try :
          xvalue = float(df_corr[xkey].loc[year])
          if not np.isnan(xvalue):
            comparematrix[0].append(xvalue)
            comparematrix[1].append(float(df_corr[ykey].loc[year]))
            break
        except KeyError as e :
          if len(comparematrix[0]) > len(comparematrix[1]) :
            comparematrix[0].pop()
          elif len(comparematrix[1]) > len(comparematrix[0]) :
            comparematrix[1].pop()
          break
  return comparematrix

def get_xy_gdp(ykey, inds_df):
  '''Modified version of get_xy_lists in order to answer the question of gdp per capita spent towards education's effect '''
  xkey1 = 'GDP per capita (2011 PPP $)'
  xkey2 = 'Government expenditure on education (% of GDP)'
  xkey3 = 'Total population (millions)'
  comparematrix = [[],[]]
  print(comparematrix)
  for i in country_names :
    df_corr = plot_corr_country(inds_df, i)
    if xkey in df_corr :
      for yearnum in range(2013, 2016):
        year = str(yearnum)
        try :
          gdppercap = float(df_corr[xkey1].loc[year]) * float(df_corr[xkey2].loc[year])/100
          if not np.isnan(gdppercap):
            if gdppercap > 4000 :
              print(i, gdppercap, float(df_corr[ykey].loc['2015']))
            #print((float(df_corr[xkey1].loc[year])/100) * float(df_corr[xkey2].loc[year]) * float(df_corr[xkey3].loc[year]))
            comparematrix[0].append(gdppercap)
            comparematrix[1].append(float(df_corr[ykey].loc['2015']))
            break
        except KeyError as e :
          if len(comparematrix[0]) > len(comparematrix[1]) :
            comparematrix[0].pop()
          elif len(comparematrix[1]) > len(comparematrix[0]) :
            comparematrix[1].pop()
          break
  return comparematrix

def plot_xy_gdp(ykey='Programme for International Student Assessment (PISA) score in mathematics', inds_df):
  comparematrix = get_xy_gdp(ykey, inds_df)

  plt.xlabel('% GDP per capita spent on education ')
  plt.ylabel(ykey)

  pairs = sorted(list(zip(comparematrix[0], comparematrix[1])), key=lambda x: x[0])
  comparematrix[0], comparematrix[1] = zip(*pairs)
  comparematrix[0] =list(comparematrix[0])
  comparematrix[1] =list(comparematrix[1])
  comparematrix[0].pop()
  comparematrix[1].pop()
  plt.scatter(comparematrix[0], comparematrix[1])
  boundary = 32
  plt.plot(np.unique(comparematrix[0][0:boundary]), np.poly1d(np.polyfit(comparematrix[0][0:boundary], comparematrix[1][0:boundary], 1))(np.unique(comparematrix[0][0:boundary])))
  plt.plot(np.unique(comparematrix[0][boundary:]), np.poly1d(np.polyfit(comparematrix[0][boundary:], comparematrix[1][boundary:], 1))(np.unique(comparematrix[0][boundary:])))
  # basically qatar has a lot of money but pisa scores were bad, although it has been improving a lot, 20 point increase past 3 years