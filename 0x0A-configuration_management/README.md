<h1 class="gap">0x0A Configuration management</h1>

<h2>Background Context</h2>

<p><a href="https://youtu.be/ogYLFyp68cI" target="_blank"><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/6/6a0a8024f2b1c47a9d1e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201207%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201207T221150Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=57fe2f349c77286639d81b2fd72fc25b34caf1936ce327871413b49fd9361fb5" alt="" style="" /></a></p>

<p>When I was working for SlideShare, I worked on an auto-remediation tool called <a href="/rltoken/ftFvBjxNPLoWcF9eHaK8yw" title="Skynet" target="_blank">Skynet</a> that monitored, scaled and fixed Cloud infrastructure. I was using a parallel job-execution system called MCollective that allowed me to execute commands to one or multiple servers at the same time. I could apply an action to a selected set of servers by applying a filter such as the server&rsquo;s hostname or any other metadata we had (server type, server environment&hellip;). At some point, a bug was present in my code that sent <code>nil</code> to the filter method. </p>

<p>There were 2 pieces of bad news:</p>

<ol>
<li>When MCollective receives <code>nil</code> as an argument for its filter method, it takes this to mean &lsquo;all servers&rsquo;</li>
<li>The action I sent was to terminate the selected servers</li>
</ol>

<p>I started the parallel job-execution and after some time, I realized that it was taking longer than expected. Looking at logs I realized that I was shutting down SlideShare&rsquo;s entire document conversion environment. Actually, 75% of all our conversion infrastructure servers had been shut down, resulting in users not able to convert their PDFs, powerpoints, and videos&hellip; Pretty bad!</p>

<p>Thanks to Puppet, we were able to restore our infrastructure to normal operation in under 1H, pretty impressive. Imagine if we had to do everything manually: launching the servers, configuring and linking them, importing application code, starting every process, and obviously, fixing all the bugs (you should know by now that complicated infrastructure always goes sideways)&hellip;</p>

<p>Obviously writing Puppet code for your infrastructure requires an investment of time and energy, but in the long term, it is for sure a must-have.</p>

<p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/292/4i8il3B.gif" alt="" style="" /></p>

<p><a href="/rltoken/uHU1llO2UZXg8_funEgpJA" title="https://twitter.com/devopsreact/status/836971570136375296" target="_blank"></a></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/r-NmkYO8bxIKp2qEx2ZjKQ" title="Intro to Configuration Management" target="_blank">Intro to Configuration Management</a> </li>
<li><a href="/rltoken/fuhnsI9_1_F4GrHwGT3GxA" title="Puppet resource type: file" target="_blank">Puppet resource type: file</a> (<em>check &ldquo;Resource types&rdquo; for all manifest types in the left menu</em>)</li>
<li><a href="/rltoken/Fqmb5rnChQgYAypvKoTxAQ" title="Puppet&#39;s Declarative Language: Modeling Instead of Scripting" target="_blank">Puppet&rsquo;s Declarative Language: Modeling Instead of Scripting</a></li>
<li><a href="/rltoken/oezu0m_hJ8nEVA6a9o17Tw" title="Puppet lint" target="_blank">Puppet lint</a> </li>
<li><a href="/rltoken/N70cVw8mG3707He-OxjP1w" title="Puppet emacs mode" target="_blank">Puppet emacs mode</a> </li>
</ul>