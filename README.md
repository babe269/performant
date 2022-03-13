# performant
## A toolset for easy formant extraction and visualization from wav files and TTS models

Performant is a tool to extract formant data and visualise vowel space in python. It utilises the BAS WebMausBasic API along side Praat's formant tracking alogrithm to create a
streamline process of obtaining formants directly from audio and text inputs. 

## Installation 
### With pip 
`$ pip install performant` </br>

then: </br>

`from performant install tools`

in your python code. 

### From Source
Examples of how to call functions are illustrated below. Clone the repository and use the [tools script](performant/src/performant/tools.py) for the desired function.
```
$ git clone https://github.com/babe269/performant
$ cd performant
$ pip install . 
```
To upgraade the repository and all dependancies

``` 
$git pull
$git install -- upgrade .
```
## Usage
performant contains two functions located in the [tools.py](performant/src/performant/tools.py) script.
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

The function is stuctured like this: </br>
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
- <b>centroid:</b> boolean corresponding to avaraging repeat vowel data.
  - This setting is based on personal preference. If you want all formant values leave this `False`. If you want one averaged value for each input vowel change this to `True`
  
  
and it has two output argument:
- <b>formants:</b> a <a href=https://pandas.pydata.org>Pandas</a> dataframe of the requested vowels and the corresponding first (F1) and second formant (F2) values for each.
- <b>figure:</b> an interactive <a href=https://plotly.com>Plotly</a> Vowel Space plot of F1 against F2:
  
  
### plotPath()
This function allows for comparison of organised samples, usually two different speakers. This function was designed for formant analysis in synthetic speech but is applicable to
human speech aswell. Use this function when you wish to see the difference between two or more organised sets of speech samples. 

For this example,imagine two speakers, A and B. We have sample from both and we wish to see the difference between these two speakers on a vowel space

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
same as before, ensure that all the speech samples and transcript pairs have the same name. This name can be reapeated from speaker to speaker but two should not have the same name within the same
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

Note that this function autmatically creates a centroid value of each vowel for each speaker.

## Contact: 
me: babe269@aucklanduni.ac.nz
