# performant
## A toolset for easy formant extraction and visualization.

Performant is a tool to extract formant data and visualise vowel space in python. It utilises the BAS WebMausBasic API along side Praat's formant tracking algorithm to create a streamline process of obtaining formants directly from audio and text inputs. 

![newplot (27)](https://user-images.githubusercontent.com/48380210/159826418-f3c446e7-9524-43c4-926b-cfb2a0f50b08.png)

peformant streamlines the process of obtaining formant data in python and allows easy visualisation to develop and understanding of how a speaker sounds.
Formants are a range of frequencies in which there is absolute or relative maximum in the sound spectrum. The frequency at the maximum is the formant frequency . The first formant(F1), corresponds to the vertical position of the tongue body within the mouth and typically associated with frequencies between 200 and 900 Hz. The second formant (F2), corresponds to the horizontal position of the tongue body within the mouth and refers to frequencies between 1300 - 2600 Hz for New Zealand English. The position of the tongue in the mouth constricts air flow within the throat and the roof of the mouth adjusting the frequency of the air as it passes through. A large part of voiced sections in human speech are attributed to vowels, and vowels often exhibit noticeable change in first and the second formant frequencies. 



Additionally, performant can be used in organised groups of data, such as comparing speakers and even machine learning models. This can be used to visualise the process of speaker adaptation as shown here
![evolution](https://user-images.githubusercontent.com/48380210/159627683-15f88cc7-9e6d-4acf-be93-db2e58ae596d.gif)

In the above example, performant can be used to show how speaker adaptaion between US and NZE for Tacotron 2 can be visualised in a vowel space. 
(For more information on this study see XXXX)

## Installation 
### With pip 
`$ pip install performant-babe269` </br>

then: </br>

`from performant import tools`

in your python code. 


### From Source
Examples of how to call functions are illustrated below. Clone the repository and use the [tools script](/src/performant/tools.py) for the desired function.
```
$ git clone https://github.com/babe269/performant
$ cd performant
$ pip install . 
```
To upgrade the repository and all dependencies

``` 
$git pull
$git install -- upgrade .
```
## Usage
performant contains two functions located in the [tools.py](/src/performant/tools.py) script.
- `plotFormants()` 
- `plotPath()`

### plotFormants()
This funtion is used for general puprose formant extraction and plotting. It takes in a speech sample and their corresponding text transcription and plots its respective formants
It is also cabable of batch extraction and formant averaging across multiple samples.

For this example, imagine three samples of a New Zealand English (NZE) speaker that you wished to obtain the formants form.

Please prepare your data set in the following file structure.
```
|- [Samples]/
|   |- sample1.wav
|   |- sample1.txt
|   |- sample2.wav
|   |- sample2.txt
|   |- sample3.wav
|   |- sample3.txt
```
Ensure that all samples that wish to be processed have both their wav and txt transcription in the parent folder and that they have the same name.This structure is the same
regardless of how many files you wish to process at once.</br> After this, please navigate into this directory before using the `plotFormants()` function.
In this example it would be 

`$ cd Samples `

The function is structured like this: </br>
`dataframe, figure = plotFormants([fileNames], [vowels], language, centroid)`</br>
For this example the function call would look like this:</br>
`df, fig = plotFormants(["sample1", "sample2", "sample3"],["{", "}:","3:","6","6:","e","I", "i:", "O", "o:", "U" ], "eng-NZ", True)`
Lets break down each parameter:

The `plotFormants()` function takes four input arguments:
- <b>fileNames:</b> an array of the <i>unique</i> file names in the directory.
  - For the above example, this would be an array like `["sample1", "sample2", "sample3]`
- <b>vowels:</b> an array of the vowels that you wish to be extracted/plotted.
  - For the above example, NZE contains `["{", "}:","3:","6","6:","e","I", "i:", "O", "o:", "U" ]`
- <b>language:</b> string corresponding to the language of the input data.
  - This is based on Web Maus basic language setting. For a full list of supported languages see the runMAUSBasic section of the <a href="https://clarin.phonetik.uni-muenchen.de/BASWebServices/services/help">BAS API Documentation<a>.</br>
  For the above example, being NZE it would be `"eng-NZ"`
- <b>centroid:</b> boolean corresponding to averaging repeat vowel data.
  - This setting is based on personal preference. If you want all formant values leave this `False`. If you want one averaged value for each input vowel change this to `True`
  
  
and it has two output argument:
- <b>formants:</b> a <a href=https://pandas.pydata.org>Pandas</a> dataframe of the requested vowels and the corresponding first (F1) and second formant (F2) values for each.
- <b>figure:</b> an interactive <a href=https://plotly.com>Plotly</a> Vowel Space plot of F1 against F2:
  
  
### plotPath()
This function allows for comparison of organised samples, usually two different speakers. This function was designed for formant analysis in synthetic speech but is applicable to
human speech as well. Use this function when you wish to see the difference between two or more organised sets of speech samples. 

For this example, imagine two speakers, A and B. We have sample from both and we wish to see the difference between these two speakers on a vowel space

Note that this function is not limited to two speakers and additional speakers should be added in the same manner as below.

Please prepare your data set in the following file structure.
```
|- [Speakers]/
|   |- SpeakerA/
|       |- sample1.wav
|       |- sample1.txt
|       |- ...
|   |- SpeakerB/
|       |- sample1.wav
|       |- sample1.txt
|       |- ...
```
same as before, ensure that all the speech samples and transcript pairs have the same name. This name can be repeated from speaker to speaker but two should not have the same name within the same
speakers folder. Once again, navigate into this directory prior to using the `plotPath` function.

`$ cd Speakers `

The function is stuctured like this: </br>
`dataframe, figure = plotPath([folderNames], [vowels], language)`</br>
For this example the function call would look like this:</br>
`df, fig = plotPath( ['SpeakerA', 'SpeakerB'],["{", "}:","3:","6","6:","e","I", "i:", "O", "o:", "U" ], "eng-NZ")`
Lets break down each parameter:

The `plotPath()` function takes three input arguments:
- <b>folderNames:</b> an array of the sub-folders corresponding to each speaker in the directory.
  - For the above example, this would be an array like `['SpeakerA', 'SpeakerB']`
- <b>vowels:</b> an array of the vowels that you wish to be extracted/plotted.
  - For the above example, NZE contains `["{", "}:","3:","6","6:","e","I", "i:", "O", "o:", "U" ]`
- <b>language:</b> string corresponding to the language of the input data.
  - This is based on Web Maus basic language setting. For a full list of supported languages see the runMAUSBasic section of the <a href="https://clarin.phonetik.uni-muenchen.de/BASWebServices/services/help">BAS API Documentation<a>.</br>
  For the above example, being NZE it would be `"eng-NZ"`
  

and it has two output argument:
- <b>formants:</b> a <a href=https://pandas.pydata.org>Pandas</a> dataframe of the requested vowels and the corresponding first (F1) and second formant (F2) values for each.
- <b>figure:</b> an interactive <a href=https://plotly.com>Plotly</a> Vowel Space plot of F1 against F2:

Note that this function automatically creates a centroid value of each vowel for each speaker.

## How to Cite
If you wish to cite performant, you may cite this study accpeted to Interspeech 2022: 
  Abeysinghe B. N., James J, Watson C, and Marattukalam F, Visualising Model Training via Vowel Space for Text-To-Speech Systems, Accepted to Proc. Interspeech 2022 
 
## Contact: 
me: babe269@aucklanduni.ac.nz
