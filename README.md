# AlbumClasse
An image classifier for album covers! I wanted to make something that would classify different genre’s of their album based on their art. Will be using Google’s Teachable Machine interface to build our model.

As someone who is incredibly passionate and fascinated by the world of music, this project will allow me to align and apply the learnings of this class with the areas of life which interest us most. One of the things that has most attracted me to the artistic component of music is how messages or themes regarding an album can be established or further portrayed through the album artwork. I wanted to see if this artwork was noticeable distingushable between genres.


## Process 
1. I began with a test of the teachable machine, creating 3 genre categories and uploading about 10 albums for each genre to train the machine on. This was a successful test, though the teachable machine was not accurate.
2. The second step of the process involved collecting more images to train the teachable machine with. I developed a webscraper.py above to download album artwork en mass, allowing a large amount of data to be collected in a very short time. 
3. Using this script, I downloaded between 250-500 album covers for each of three genres: Jazz, Rap, and Rock. 
4. Revisiting the teachable machine, we created three classification categories and trained them on the around 80% of album covers we collected for each genre. We were then able to upload an album cover to the teachable machine and have it attempt to classify the album. 
5. We then used the Machine to test the classification accuracy rate of the remaining 20% of the album covers we had downloaded, and saw accuracy results of close to 70% for Rap and Rock, and just over 50% for Jazz.
