<h1 class="gap">0x06. Regular expression</h1>

 <h2>Background Context</h2>

<p>For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.</p>

<p>Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the <code>//</code>:</p>

<pre><code>sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
</code></pre>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/SJ2eQ7V2iQlCgLc-L96zWg" title="Regular expressions - basics" target="_blank">Regular expressions - basics</a> </li>
<li><a href="/rltoken/qyjWL-J1_qUaZGR690gH1Q" title="Regular expressions - advanced" target="_blank">Regular expressions - advanced</a> </li>
<li><a href="/rltoken/WCjn8NgohbQ5NGXEObWZvQ" title="Rubular is your best friend" target="_blank">Rubular is your best friend</a> </li>
<li><a href="/rltoken/Zfvv_ydOCvJ_YaBB6eDqVw" title="Use a regular expression against a problem: now you have 2 problems" target="_blank">Use a regular expression against a problem: now you have 2 problems</a> </li>
<li><a href="/rltoken/Y-OVGcJ5cskdXWIBowiE_A" title="Learn Regular Expressions with simple, interactive exercises" target="_blank">Learn Regular Expressions with simple, interactive exercises</a> </li>
</ul>

<h4 class="task">
    0. Simply matching Holberton
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>
  <p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/ec65557f0da1fbfbff6659413885e4d4822f5b1d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201109%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201109T162805Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a22afc38c1fe09cb32033fd03459d5c230c5fc4ad67e91d9d18c7e703a126550" alt="" style="" /></p>

<h4 class="task">
    1. Repetition Token #0
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  <p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/e7db3c377d46453588fc84f3a975661d142fee91.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201109%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201109T162805Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4bdd29bebd2ce8078aca305d0172338edc82cdeb252d0b023a8d30289ef3ed5e" alt="" style="" /></p>

<h4 class="task">
    2. Repetition Token #1
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  <p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/c59ff11db195d5cf17d1790a5141ae2f234786d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201109%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201109T162806Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ed7795dc8ce41630fa92916b800cfcf76899a5f6b284260fb50cdd60946769a5" alt="" style="" /></p>

<h4 class="task">
    3. Repetition Token #2
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  <p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/3b6bf4aeca6a0c2de584e7f5d68d11eef57ce205.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201109%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201109T162806Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=301c8f0aa6e5800d66599b0162122515db9a2405f9f1c7fa2dd3042f1616b80e" alt="" style="" /></p>

 <h4 class="task">
    4. Repetition Token #3
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  <p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/f8dbcb9cf5ae569a8645027dc46e81cb372ce28e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201109%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201109T162806Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=060f569a6c9ec357949563ebf099c22b49db8a980fbf970731e4e2ddc482ff55" alt="" style="" /></p>

<h4 class="task">
    5. Not quite HBTN yet
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

<h4 class="task">
    6. Call me maybe
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  <p>This task is brought to you by Holberton professional advisor <a href="/rltoken/V4rEpseJEPRMMnfaZPbkgw" title="Neha Jain" target="_blank">Neha Jain</a>, Senior Software Engineer at LinkedIn.</p>
