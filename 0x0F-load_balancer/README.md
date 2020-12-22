<h1 class="gap">0x0F. Load balancer</h1>

            <em><a href="/concepts/46">Load balancer</a></em>
          </li>
          <li>
            <em><a href="/concepts/68">Web stack debugging</a></em>
          </li>
      </ul>
    </div>

  <article id="description" class="gap formatted-content">
    <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/275/qfdked8.png" alt="" style="" /></p>

<h2>Background Context</h2>

<p>You have been given 2 additional servers:</p>

<ul>
<li>gc-[STUDENT_ID]-web-02-XXXXXXXXXX</li>
<li>gc-[STUDENT_ID]-lb-01-XXXXXXXXXX</li>
</ul>

<p>Let&rsquo;s improve our web stack so that there is <a href="/rltoken/QiOC_I-8BeV4aNExIucC9Q" title="redundancy" target="_blank">redundancy</a> for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.</p>

<p>For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.</p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/ngIXarEyu8jZwOL3Y30PLQ" title="Introduction to load-balancing and HAproxy" target="_blank">Introduction to load-balancing and HAproxy</a> </li>
<li><a href="/rltoken/v32JmcDrSiOnFBfqzXvs_Q" title="HTTP header" target="_blank">HTTP header</a> </li>
<li><a href="/rltoken/BXGrW_6ocecWaOJb7OK_WA" title="Debian/Ubuntu HAProxy packages" target="_blank">Debian/Ubuntu HAProxy packages</a></li>
</ul>