def actors():
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
					<a href="characters.html"><img src="z/logo.svg" width="250" alt="my logo"></a>
				<td>
				
				<td><h1>THE GREAT DETECTIVE</h1></td>
				
				<td>
					<a href="movies.html"><img src="z/logo.svg" width="250" alt="my logo"></a>
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
		
		<table id="maincharacters">
			
			<thead style="color:brown">
				<tr>
					<th>Character</th>
					<th>Artist</th>
					<th>Year</th>
					<th>Type</th>
				</tr>
			</thead>
			
			<tbody>
				<tr>
					<td rowspan="28">Sherlock Holmes</td>
					<td>C.H.E. Brookfield</td>
					<td>1893</td>
					<td rowspan="13">Stage</td>
				</tr>
				
				<tr>
					<td>John F. Preston</td>
					<td>1900</td>
				</tr>
				
				<tr>
					<td>Károly Baumann</td>
					<td>1905</td>
				</tr>
				
				<tr>
					<td>Dennis Neilson-Terry</td>
					<td>1921</td>
				</tr>
				
				<tr>
					<td>Tod Slaughter</td>
					<td>1928</td>
				</tr>	
				
				<tr>
					<td>Basil Rathbone</td>
					<td>1953</td>
				</tr>	
				
				<tr>
					<td>John Wood</td>
					<td>1974</td>
				</tr>
				
				<tr>
					<td>Paxton Whitehead</td>
					<td>1978</td>
				</tr>
				
				<tr>
					<td>Tom Baker</td>
					<td>1985</td>
				</tr>
				
				<tr>
					<td>Ron Moody</td>
					<td>1989</td>
				</tr>
				
				<tr>
					<td>Benjamin Lawlor</td>
					<td>2013</td>
				</tr>
				
				<tr>
					<td>Gregory Wooddell</td>
					<td>2015</td>
				</tr>
				
				<tr>
					<td>Jay Taylor</td>
					<td>2018</td>
				</tr>
				
				<tr>
					<td>Alan Napier</td>
					<td>1949</td>
					<td rowspan="15">TV Series</td>
				</tr>
				
				<tr>
					<td>Basil Rathbone</td>
					<td>1953</td>
				</tr>
				
				<tr>
					<td>Douglas Wilmer</td>
					<td>1964</td>
				</tr>
				
				<tr>
					<td>Peter Cushing</td>
					<td>1968</td>
				</tr>
				
				<tr>
					<td>Geoffrey Whitehead</td>
					<td>1979</td>
				</tr>
				
				<tr>
					<td>Peter Lawford</td>
					<td>1982</td>
				</tr>
				
				<tr>
					<td>Jeremy Brett</td>
					<td>1984</td>
				</tr>
			
				<tr>
					<td>Brian Bedford</td>
					<td>1989</td>
				</tr>
				
				<tr>
					<td>Jeremy Brett</td>
					<td>1994</td>
				</tr>
			
				<tr>
					<td>Robert Webb</td>
					<td>2007</td>
				</tr>
			
				<tr>
					<td>Alexander Armstrong</td>
					<td>2010</td>
				</tr>
			
				<tr>
					<td>Benedict Cumberbatch</td>
					<td>2010</td>
				</tr>
			
				<tr>
					<td>Igor Petrenko</td>
					<td>2013</td>
				</tr>
			
				<tr>
					<td>Mark Caven</td>
					<td>2016</td>
				</tr>
			
				<tr>
					<td>Ewan Bremner</td>
					<td>2016</td>
				</tr>
			
				<tr>
					<td rowspan="20">Dr. John Watson</td>
					<td>Seymour Hicks</td>
					<td>1893</td>
					<td rowspan="10">Stage</td>
				</tr>
				
				<tr>
					<td>Bruce McRae</td>
					<td>1899</td>
				</tr>
				
				<tr>
					<td>H. G. Stoker</td>
					<td>1923</td>
				</tr>
				
				<tr>
					<td>Peter Sallis</td>
					<td>1965</td>
				</tr>
				
				<tr>
					<td>Dennis Cooney</td>
					<td>1974</td>
				</tr>	
				
				<tr>
					<td>Richard Woods</td>
					<td>1981</td>
				</tr>
				
				<tr>
					<td>Alan Stanford	</td>
					<td>1985</td>
				</tr>
				
				<tr>
					<td>Donal Donnelly</td>
					<td>1987</td>
				</tr>
				
				<tr>
					<td>Lucas Hall</td>
					<td>2015</td>
				</tr>
				
				<tr>
					<td>Patrick Robinson</td>
					<td>2017</td>
				</tr>
				
				<tr>
					<td>Melville Cooper</td>
					<td>1949</td>
					<td rowspan="10">TV Series</td>
				</tr>
				
				<tr>
					<td>Jack Raine</td>
					<td>1953</td>
				</tr>
				
				<tr>
					<td>Nigel Stock</td>
					<td>1965</td>
				</tr>
				
				<tr>
					<td>Gianni Bonagura</td>
					<td>1968</td>
				</tr>
				
				<tr>
					<td>Donald Pickering</td>
					<td>1979</td>
				</tr>
				
				<tr>
					<td>Vitaly Solomin</td>
					<td>1979</td>
				</tr>
				
				<tr>
					<td>David Burke	</td>
					<td>1984</td>
				</tr>
				
				<tr>
					<td>Edward Hardwicke</td>
					<td>1986</td>
				</tr>
				
				<tr>
					<td>Patrick Monckton</td>
					<td>1989</td>
				</tr>
				
				<tr>
					<td>Martin Freeman</td>
					<td>2010</td>
				</tr>
				
				<tr>
					<td rowspan="20">Mrs. Hudson</td>
					<td>Mary Holder</td>
					<td>1964</td>
					<td rowspan="20">TV Series</td>
				</tr>
				
				<tr>
					<td>Enid Lindsey</td>
					<td>1965</td>
				</tr>
				
				<tr>
					<td>Manja Kafka</td>
					<td>1967</td>
				</tr>
				
				<tr>
					<td>Edda Urusova</td>
					<td>1968</td>
				</tr>
				
				<tr>
					<td>Grace Arnold</td>
					<td>1968</td>
				</tr>
				
				<tr>
					<td>Gisela Hoeter</td>
					<td>1974</td>
				</tr>
				
				<tr>
					<td>Connie Booth</td>
					<td>1977</td>
				</tr>
				
				<tr>
					<td>Rina Zelyonaya</td>
					<td>1979</td>
				</tr>
				
				<tr>
					<td>Kay Walsh</td>
					<td>1979</td>
				</tr>
				
				<tr>
					<td>Jenny Laird</td>
					<td>1984</td>
				</tr>
				
				<tr>
					<td>Rosalie Williams</td>
					<td>1984</td>
				</tr>
				
				<tr>
					<td>Lila Kaye</td>
					<td>1987</td>
				</tr>
				
				<tr>
					<td>Faith Kent</td>
					<td>1990</td>
				</tr>
				
				<tr>
					<td>Margaret John</td>
					<td>1992</td>
				</tr>
				
				<tr>
					<td>Sophia Thornley</td>
					<td>1993</td>
				</tr>
				
				<tr>
					<td>Kathleen McAuliffe</td>
					<td>2001</td>
				</tr>
				
				<tr>
					<td>Geraldine James</td>
					<td>2009</td>
				</tr>
				
				<tr>
					<td>Catriona McDonald</td>
					<td>2010</td>
				</tr>
				
				<tr>
					<td>Una Stubbs</td>
					<td>2010</td>
				</tr>
				
				<tr>
					<td>Ingeborga Dapkunaite</td>
					<td>2013</td>
				</tr>
				
				<tr>
					<td colspan="4">TO BE CONTINUED...</td>
				</tr>
			</tbody>	
		</table>
		
	</body>
</html>
"""
    return page
