<h1 class="gap">0x05. Processes and signals</h1>

 <h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/FcpEdqz8hau7eEB0Pi8Ong" title="Linux PID" target="_blank">Linux PID</a> </li>
<li><a href="/rltoken/hX_t2YK0erLPbdTq0-uKwQ" title="Linux process" target="_blank">Linux process</a> </li>
<li><a href="/rltoken/SojW4zvL8j1yaoa7_NM6rA" title="Linux signal" target="_blank">Linux signal</a> </li>
</ul>

 <h4 class="task">
    0. What is my PID
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  <p>Write a Bash script that displays its own PID.</p>

 <h4 class="task">
    1. List your processes
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  <p>Write a Bash script that displays a list of currently running processes.</p>

<h4 class="task">
    2. Show your Bash PID
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  <p>Using your previous exercise command, write a Bash script that displays lines containing the <code>bash</code> word, thus allowing you to easily get the PID of your Bash process.</p>

  3. Show your Bash PID made easy
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  <p>Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word <code>bash</code>.</p>

<p>Requirements:</p>

<ul>
<li>You cannot use <code>ps</code></li>
</ul>

 <h4 class="task">
    4. To infinity and beyond
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  <p>Write a Bash script that displays <code>To infinity and beyond</code> indefinitely. </p>

<h4 class="task">
    5. Don&#39;t stop my now!
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  <p>We stopped our <code>4-to_infinity_and_beyond</code> process using <code>ctrl+c</code> in the previous task, there is actually another way to do this.</p>

 <h4 class="task">
    6. Stop me if you can
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  <p>Write a Bash script that stops <code>4-to_infinity_and_beyond</code> process.</p>

 <h4 class="task">
    7. Highlander
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  <p>Write a Bash script that displays: </p>

<ul>
<li><code>To infinity and beyond</code> indefinitely</li>
<li>With a <code>sleep 2</code> in between each iteration</li>
<li><code>I am invincible!!!</code> when receiving a <code>SIGTERM</code> signal</li>
</ul>

 <h4 class="task">
    8. Beheaded process
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  <p>Write a Bash script that kills the process <code>7-highlander</code>.</p>

<h4 class="task">
    9. Process and PID file
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
  </h4>

  <p>Write a Bash script that: </p>

<h4 class="task">
    10. Manage my process
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
  </h4>

  <p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/37975393ead381f4d27f268f7337c6d3013b4991.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201026%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201026T140336Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=81666aab16eeab167341521e1b07585267ce66c3f6950414d735815726ed85b3" alt="" style="" /></p>

<p>Read:</p>

<ul>
<li><a href="/rltoken/ISCvYLlssHBRk3117QINuw" title="&amp;" target="_blank">&amp;</a></li>
<li><a href="/rltoken/YhzaWR9jdFi2W0d0qrNJ3w" title="init.d" target="_blank">init.d</a></li>
<li><a href="/rltoken/mNOdP_7ieM7KQaNHh504NA" title="Daemon" target="_blank">Daemon</a></li>
<li><a href="/rltoken/YPgjXhBUEDN1yh1rkQOe1w" title="Positional parameters" target="_blank">Positional parameters</a></li>
</ul>

<p>man: <code>sudo</code></p>

<p>Programs that are detached from the terminal and running in the background are called daemons or processes, need to be managed. The general minimum set of instructions is: <code>start</code>, <code>restart</code> and <code>stop</code>. The most popular way of doing so on Unix system is to use the init scripts.</p>

<p>Write a <code>manage_my_process</code> Bash script that: </p>

<h4 class="task">
    11. Zombie
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
  </h4>

  <p><a href="http://fineartamerica.com/featured/zombie-seahorse-lauren-b.html" target="_blank"><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/255/C6mO7b3.jpg" alt="" style="" /></a></p>

<p>Read <a href="/rltoken/lD64_7WBTGbjxM9IJ5ncdg" title="what a zombie process is" target="_blank">what a zombie process is</a>.</p>

<p>Write a C program that creates 5 zombie processes.</p>

<h4 class="task">
    12. Screencast
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
  </h4>

  <p>Now that you have mastered signals, how about sharing your knowledge?</p>

<p>Create a screencast where you live-code/demo something related to Unix signals.</p>