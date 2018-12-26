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
					<a href="bibliography.html"><img src="z/logo.svg" width="250" alt="my logo"></a>
				</td>
				
				<td><h1>THE GREAT DETECTIVE</h1></td>
				
				<td>
					<a href="characters.html"><img src="z/logo.svg" width="250" alt="my logo"></a>
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
				
		<p class="homep">
		Sherlock Holmes is a fictional private detective created by
		British author <span class="span">Sir Arthur Conan Doyle
		</span>. Referring to himself as a <span class="span">
		"consulting detective"</span> in the stories, Holmes is known
		for his proficiency with observation, forensic science, and
		logical reasoning that borders on the fantastic, which he
		employs when investigating cases for a wide variety of clients,
		including Scotland Yard.</p>
		
		<p class="homep">
		First appearing in print in 1887's <span class="span">
		A Study in Scarlet</span>, the character's popularity became
		widespread with the first series of short stories in The Strand
		Magazine, beginning with <span class="span">"A Scandal in
		Bohemia"</span> in 1891; additional tales appeared from then
		until 1927, eventually totalling four novels and 56 short
		stories. All but one are set in the Victorian or Edwardian eras,
		between about 1880 and 1914. Most are narrated by the character
		of Holmes's friend and biographer <span class="span">
		Dr. Watson</span>, who usually accompanies Holmes during his
		investigations and often shares quarters with him at the address
		of <span class="span"> <a href="https://www.google.com.tr/maps/place/221B+Baker+St,+Marylebone,+London+NW1+6XE,+UK/@51.5237135,-0.1606426,17z/data=!3m1!4b1!4m5!3m4!1s0x48761acf347aba15:0x5c42845f6914e674!8m2!3d51.5237102!4d-0.1584593"
		style="text-decoration:none">221B Baker Street, London</a></span>
		,where many of the stories begin.</p>
		
		<p class="homep">
		Though not the first fictional detective, Sherlock Holmes is
		arguably the best known, with Guinness World Records listing him
		as the <span class="span">"most portrayed movie character"
		</span>in history. Holmes's popularity and fame are such that
		many have believed him to be not a fictional character but a
		real individual; numerous literary and fan societies have been
		founded that pretend to operate on this principle. Widely
		considered a British cultural icon, the character and stories
		have had a profound and lasting effect on mystery writing and
		popular culture as a whole, with the original tales as well as
		thousands written by authors other than Conan Doyle being
		adapted into stage and radio plays, television, films,
		video games, and other media for over one hundred years.</p>
        
        <form action="/index.html" method="post">
            <fieldset>
                <legend>Would you like say anything</legend>
                What is your comment?
                <br>
                <input type="text" name="comment">
                <br>
                Enter your password please.
                <br>
                <input tppe="text" name="password">
                <br>
                <input type=submit value="SEND">
            </fieldset>
        </form>
        
        <ul>
			%s
        </ul>
	</body>
</html>
"""
def index():
	return page %(end)

#this part is taken from
# https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py
from hashlib import sha256

def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()
########

from bottle import request

mypassword = 'f155a9176a400fd61286391e4cb7dfba3b139fffcf6bc219cd258981cc01c628'

comments = []
end = ""

def is_it_true():
	global comments, end
	a = request.forms.get('comment')
	b = request.forms.get('password')
	
	if create_hash(b) == mypassword:
		comments = comments + [a]
	
	end = ""
	for com in comments:
		end += "<li>" + com + "</li>"
	
	return page %(end)
