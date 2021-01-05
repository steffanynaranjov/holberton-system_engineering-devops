<h1 class="gap">0x13. Firewall</h1>

<h2>Background Context</h2>

<h3>Your servers without a firewall&hellip;</h3>

<p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/155/holbertonschool-firewall.gif" alt="" style="" /></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/QS5iHSDU_woydPRIb68sOw" title="What is a firewall" target="_blank">What is a firewall</a> </li>
</ul>

<h2>More Info</h2>

<p>As explained in the <strong>web stack debugging guide</strong> concept page, <code>telnet</code> is a very good tool to check if sockets are open with <code>telnet IP PORT</code>. For example, if you want to check if port 22 is open on <code>web-02</code>:</p>

<pre><code>sylvain@ubuntu$ telnet web-02.holberton.online 22
Trying 54.89.38.100...
Connected to web-02.holberton.online.
Escape character is &#39;^]&#39;.
SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.8

Protocol mismatch.
Connection closed by foreign host.
sylvain@ubuntu$
</code></pre>

<p>We can see for this example that the connection is successful:
<code>Connected to web-02.holberton.online.</code></p>

<p>Now let&rsquo;s try connecting to port 2222:</p>

<pre><code>sylvain@ubuntu$ telnet web-02.holberton.online 2222
Trying 54.89.38.100...
^C
sylvain@ubuntu$
</code></pre>