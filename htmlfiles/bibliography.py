def bibliography():
    page="""
<!DOCTYPE html>
	
<html lang="en">
		
	<head>
		<meta charset="utf-8">
		<title>SHERLOCK HOLMES</title>
		<link rel="stylesheet" href="sherlock.css">
	</head>
	
	<body>
		
		<table id="logo">
			<tr>
				<td>
					<a href="gallery.html"><img src="z/logo.svg" width="250" alt="my logo"></a>
				</td>
				
				<td><h1>THE GREAT DETECTIVE</h1></td>
				
				<td>
					<a href="index.html"><img src="z/logo.svg" width="250" alt="my logo"></a>
				</td>
			</tr>
		</table>
		
		<table id="menu">
			<tr>
				<td> <a href="index.html"
						style="text-decoration:none">Home</a> </td>
				<td> <a href="characters.html"
						style="text-decoration:none">Characters</a> </td>
				<td> <a href="actors.html"
						style="text-decoration:none">Actors</a> </td>
				<td> <a href="movies.html"
						style="text-decoration:none">Movies</a> </td>
				<td> <a href="gallery.html"
						style="text-decoration:none">Gallery</a> </td>
				<td> <a href="bibliography.html"
						style="text-decoration:none">Bibliography</a> </td>
			</tr>
		</table>
		
		<ol>
			<li>Home
				<ul class="resources">
					<li><a href="https://en.wikipedia.org/wiki/Sherlock_Holmes">
					https://en.wikipedia.org/wiki/Sherlock_Holmes</a>
					</li>
				</ul>
			</li>
			
			<li>Actors
				<ul class="resources">	
					<li><a href="https://en.wikipedia.org/wiki/List_of_actors_who_have_played_Sherlock_Holmes">
					https://en.wikipedia.org/wiki/List_of_actors_who_have_played_Sherlock_Holmes</a>
					</li>
			
					<li><a href="https://en.wikipedia.org/wiki/List_of_actors_who_have_played_Dr._Watson">
					https://en.wikipedia.org/wiki/List_of_actors_who_have_played_Dr._Watson</a>
					</li>
					
					<li><a href="https://www.arthur-conan-doyle.com/index.php/Gallery_of_Mrs_Hudson_performers">
					https://www.arthur-conan-doyle.com/index.php/Gallery_of_Mrs_Hudson_performers</a>
					</li>	
				</ul>
			</li>
			
			<li>Movies
				<ul class="resources">
					<li><a href="https://www.imdb.com/list/ls066973103/">
					https://www.imdb.com/list/ls066973103/</a>
					</li>
				</ul>
			</li>
		</ol>
	</body>
</html>
"""
    return page
