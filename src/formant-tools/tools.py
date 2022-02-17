def computeWav(fileNames, vowels, language, centroid):
  #Requirements if running on Colab: install !pip install praat-parselmouth !pip install tgt 
  #cd into a directory to store wav, txt and textgrid files before running. 
  import pandas as pd
  import requests
  import urllib.request 
  import parselmouth
  import tgt
  import plotly.express as px

  vl = []
  f1l = []
  f2l = []
  #List of vowels for NZE
  vowels = vowels
  
  for fileName in fileNames:
      #Call WebMaus Basic Api to generate TextGrids.

      headers = {
        'content-type': 'multipart/form-data',
      }

      files = {
        'SIGNAL': (fileName + '.wav', open(fileName + '.wav', 'rb')),
        'LANGUAGE': (None, language),
        'OUTFORMAT': (None, 'TextGrid'),
        'TEXT': (fileName + '.txt', open(fileName + '.txt', 'rb')),
      }
      result = requests.post('https://clarin.phonetik.uni-muenchen.de/BASWebServices/services/runMAUSBasic', files=files)
      decodeResponse = result.content.decode("utf-8")
      xmlSplit = decodeResponse.split("<downloadLink>")
      downURL = xmlSplit[1].split("</downloadLink>")
      downURL = downURL[0]
      urllib.request.urlretrieve(downURL, fileName+".TextGrid")
      #Use parselmouth + Textgrid tools to obtain formant information 
      ps = parselmouth.Sound(fileName + ".wav")
      formants = ps.to_formant_burg()
      tg = tgt.io.read_textgrid(fileName + '.TextGrid')
      mau = tg.get_tier_by_name("MAU")
      mauObjs = mau.intervals
      for i in vowels:
        for j in mauObjs:
          if i in j.text:
            start = j.start_time
            end = j.end_time
            mid = (start + end) / 2
            f1 = formants.get_value_at_time(1, mid, "HERTZ")
            f2 = formants.get_value_at_time(2, mid, "HERTZ")
            vl.append(j.text)
            f1l.append(f1)
            f2l.append(f2)
  #Store formant values in dataframe.
  d = {'vowel': vl, 'f1': f1l, 'f2': f2l}
  df=pd.DataFrame(d)

  if centroid == True:
    f1Centroid = df.groupby('vowel')['f1'].apply(lambda x: np.mean(x.tolist(), axis=0))
    f2Centroid = df.groupby('vowel')['f2'].apply(lambda x: np.mean(x.tolist(), axis=0))
    d = {'f1': f1Centroid, 'f2': f2Centroid}
    finaldf=pd.DataFrame(d)
    
    fig = px.scatter(finaldf, x="f2", y="f1",color= finaldf.index,  text = finaldf.index, width=800, height=700)
    fig.update_xaxes(
        tickangle = 90,
        title_text = "F2 (HZ)",
        title_font = {"size": 15},
        title_standoff = 25)
    fig.update_yaxes(
        tickangle = 90,
        title_text = "F1 (HZ)",
        title_font = {"size": 15},
        title_standoff = 25)
    fig.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    'yaxis_gridcolor':'#e5e5ea', 
    'xaxis_gridcolor':'#e5e5ea' 
    })
    fig.update_traces(textposition='top center')
    fig.update_yaxes(autorange="reversed")
    fig.update_xaxes(autorange="reversed")
    fig.update_xaxes(tickangle=0)
    fig.update_yaxes(tickangle=0)
    fig.show()
    
    
  else:
    finaldf = df

    fig = px.scatter(finaldf, x="f2", y="f1",color= "vowel",  text = "vowel", width=800, height=700)
    fig.update_xaxes(
        tickangle = 90,
        title_text = "F2 (Hz)",
        title_font = {"size": 15},
        title_standoff = 25)
    fig.update_yaxes(
        tickangle = 90,
        title_text = "F1 (Hz)",
        title_font = {"size": 15},
        title_standoff = 25)
    fig.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    'yaxis_gridcolor':'#e5e5ea', 
    'xaxis_gridcolor':'#e5e5ea' 
    })
    fig.update_traces(textposition='top center')
    fig.update_yaxes(autorange="reversed")
    fig.update_xaxes(autorange="reversed")
    fig.update_xaxes(tickangle=0)
    fig.update_yaxes(tickangle=0)
    fig.show()
    
  return finaldf