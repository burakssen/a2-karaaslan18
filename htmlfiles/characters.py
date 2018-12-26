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
					<a href="index.html"><img src="z/logo.svg" width="250" alt="my logo"></a>
				</td>
				
				<td><h1>THE GREAT DETECTIVE</h1></td>
				
				<td>
					<a href="actors.html"><img src="z/logo.svg" width="250" alt="my logo"></a>
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
		
		<dl id="definition">
			<dt class="dt">Sherlock Holmes</dt>
			<dd class="dd">
			The main character. A very very clever detective
			who can easily tell you the story of your life by using
			details that ordinary people can not realize. He do
			not have too many friends infact he has only one friend
			<span class="span">"Dr. John Watson"</span>.
			Because, when he start to talk he can
			directly break your heart by telling things that you
			do not like or he can make you fell idiot or make you angry
			cause too many people do not love clever guys.</dd>
			
			<dt class="dt">Dr. John Watson</dt>
			<dd class="dd">
			The only friend of Sherlock Holmes because he is the ony
			person who can endure to Sherlock's behaviours. Althoug
			other people do not like Sherlock he like him cause he know
			how clever he is and how a good person he is except some of
			his behaviours. Sometimes he get angry with him too but do
			not end their friendship. And,like Sherlock he love being a
			detective too.</dd>
			
			<dt class="dt">Mycroft Holmes</dt>
			<dd class="dd">
			The elder brother of Sherlock. He is very clever too and 
			generally fat. He is working for the goverment and very
			rich dislike Sherlock. Althoug he seems like he do not
			love Sherlock, he care about him and uses John Watson to
			know his status and protect him.</dd>
			
			<dt class="dt">Greg Lestrade</dt>
			<dd class="dd">
			He is an inspector in police department and one of the
			person who knows how useful Sherlock is for solving the
			case. Although he forces himself to endure his behaviours
			not to kick him, he loves Sherlock a bit cause he knows
			Sherlock is not a bad guy.
			</dd>
			
			<dt class="dt">Mrs. Hudson</dt>
			<dd class="dd">
			She is the landlady of Sherlock Holmes and extremely
			longsuffering woman. She do not love Sherlock's behaviours
			too but she care about him cause she love Sherlock a bit too.
			Although we can not see her too much in the stories we
			always know that she is there.
			</dd>
			
			<dt class="dt">Moriarty</dt>
			<dd class="dd">
			The archenemy of Sherlock Holmes. He is very clever like
			Sherlock but he is a bad guy.Infact we can call him the bad
			version of Sherlock Holmes. He hate Sherlock and John cause
			they ruin his plans,and wants to catch him. So Moriarty
			wants to kill both of them.</dd>	
			
			<dt class="dt">Irene Adler</dt>
			<dd class="dd">
			Irene Adler is a retired opera singer and actress who appears
			in <span class="span">"A Scandal in Bohemia"</span>.
			Although this is her only appearance, she is only a handful
			of people who best Holmes in a battle of wits, and the only
			woman. So she is the only woman who can earn Sherlock's
			respect with her intelligence.</dd>
		</dl>
        
        <form action="/characters.html" method="post">
            <fieldset>
                <legend>Who is your favourite character?</legend>
                <input type="radio" name="character" value="sherlock">Sherlock Holmes %d
                <input type="radio" name="character" value="john">John Watson %d
                <input type="radio" name="character" value="eurus">Eurus Holmes %d
                <input type="radio" name="character" value="mycroft">Mycroft Holmes %d
                <input type="radio" name="character" value="greg">Greg Lestrade %d
                <input type="radio" name="character" value="hudson">Mrs. Hudson %d
                <input type="radio" name="character" value="jim">Jim Moriarty %d
                <input type="radio" name="character" value="irene">Irene Adler %d
                <input type=submit value="SEND">
            </fieldset>
        </form>
	</body>
</html>
"""

s = 0
w = 0
e = 0
m = 0
g = 0
h = 0
j = 0
i = 0

def characters():
    return page %(s, w, e, m, g, h, j, i)

from bottle import request
def favourite():
    global s, w, e, m, g, h, j, i
    
    q = request.forms.get('character')
    
    if q == "sherlock":
        s += 1
    elif q == "john":
        w += 1
    elif q == "eurus":
        e += 1
    elif q == "mycroft":
        m += 1
    elif q == "greg":
        g += 1
    elif q == "hudson":
        h += 1
    elif q == "jim":
        j += 1
    elif q == "irene":
        i += 1
    return page %(s, w, e, m, g, h, j, i)
