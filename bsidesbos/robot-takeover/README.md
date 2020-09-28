# Robot Takeover

### Challenge
You know what it is, you know what to do... but can you handle the twist?

### Category
Scripting

### Connection Method
`http://challenge.ctf.games:30095/`

### Solution
1. Navigate to `robots.txt`: `http://challenge.ctf.games:30095/robots.txt`
2. Examine the response that contains dissalowed files per user agent.
```
User-agent: Mozilla/5.0 (X11; Linux i686 on x86_64; rv:5.0a2) Gecko/20110524 Firefox/5.0a2
Disallow: /6Bb2rMf53.txt
Disallow: /28GP.txt
Disallow: /NM0GlZBJ.txt
Disallow: /oMJ9TKaqAW.txt
Disallow: /HKbyoYkYQ.txt
Disallow: /YBX5CTP7hg.txt
```
3. Examine all files using the provided user agent.
4. In most cases you'll get `HELLO ROBOT. UNFORTUNATELY I DO NOT HAVE A FLAG FOR YOU HERE.`, but sometimes you'll get `REJOICE, ROBOT. THE CHARACTER OF THE FLAG AT INDEX 24 IS THE SAME CHARACTER AT INDEX 6 IN THIS FILENAME.`
5. Keep hammering until you get all characters

