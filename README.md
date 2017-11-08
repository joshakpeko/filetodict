# mangagenres
This is just a little demo of text file conversion to python dictionary object.

The input file is a list of manga anime genres with their explanations.
All terms, explanations and meanings were found and copied from
"https://reelrundown.com/animation/Anime-Genre-List".

Each genre is presented this way:
<term>
<explanation>
<examples>

The desired dictionary output looks like this:
{
  <term>: {
            "explanation": <explanation>,
            "examples": [<examples>]
          }
}

The result dictionary is saved to a .json file within the working directory.

BASIC USAGE : python3 ftodconv.py
