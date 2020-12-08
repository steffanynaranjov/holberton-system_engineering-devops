<h1 class="gap">0x0B. SSH</h1>
 <p style="margin-bottom: 0"><em>For this project, students are expected to look at this concept:</em></p>
      <ul style="margin-top: 5px">
          <li>
            <em><a href="/concepts/67">Server</a></em>
          </li>
      </ul>
    </div>

  <article id="description" class="gap formatted-content">
    <h2>Background Context</h2>

<p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/244/zPVRKhPsUP5lK.gif" alt="" style="" /></p>

<p>Along with this project, you have been attributed an Ubuntu server, living in a datacenter far far away.  Like level 2 of the application process, you will connect using <code>ssh</code>. But contrary to level 2, you will not connect using a password but an RSA key. We&rsquo;ve configured your server with the public key you created in the first task of <a href="/rltoken/LZ_8pMANOAmpn5-tiwqiJQ" title="a previous project" target="_blank">a previous project</a> shared in your <a href="/rltoken/l4Ao4ESbI_hMB6s4mjBKRw" title="intranet profile" target="_blank">intranet profile</a>.</p>

<p>You can access your server information in the <a href="/rltoken/owYhGMuyPTY4OyvSGJljGQ" title="my servers" target="_blank">my servers</a> section of the intranet, each line with contains the IP and username you should use to connect via <code>ssh</code>.</p>

<p><strong>Note:</strong> Your server is configured with an Ubuntu 16.04 LTS environment. You do <strong>not</strong> need to create a new virtual machine. If you decide you want to upgrade to Ubuntu 16.04, make sure to create a new VM. Do <strong>not</strong> attempt to upgrade your current Ubuntu 14.04 environment as that will inevitably be messy and can break things. Note that if you switch, none of your files and environment settings will be available and anything you need will have to be reinstalled or migrated.</p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/PXE-o9DWronMp4ETwADOpg" title="What is a (physical) server - text" target="_blank">What is a (physical) server - text</a> </li>
<li><a href="/rltoken/IfLc3lxSs4w5xdsFlRDPWw" title="What is a (physical) server - video" target="_blank">What is a (physical) server - video</a> </li>
<li><a href="/rltoken/qKJi0RXLqaCLkHLCLhiYNA" title="SSH essentials" target="_blank">SSH essentials</a> </li>
<li><a href="/rltoken/DNiFD9w9Gx0mnQk5nXbtjg" title="SSH Config File" target="_blank">SSH Config File</a></li>
<li><a href="/rltoken/ZBYjVLcJ-ck-CFjndgSDBw" title="Public Key Authentication for SSH" target="_blank">Public Key Authentication for SSH</a></li>
<li><a href="/rltoken/SW2m2e0KMA2K1dXk_0M0CA" title="How Secure Shell Works" target="_blank">How Secure Shell Works</a></li>
<li><a href="/rltoken/8N-RlUma9lwGfyZp1_C-Wg" title="SSH Crash Course" target="_blank">SSH Crash Course</a> (Long, but highly informative. Watch this if configuring SSH is still confusing. It may be helpful to watch at x1.25 speed or above.)</li>
</ul>

<p><strong>For reference:</strong></p>

<ul>
<li> <a href="/rltoken/6mtNBCxYkoBQJ2vJ6TcRYA" title="Understanding the SSH Encryption and Connection Process" target="_blank">Understanding the SSH Encryption and Connection Process</a></li>
<li><a href="/rltoken/c1Yj55AE6gGkDxpACdY1vg" title="Secure Shell Wiki" target="_blank">Secure Shell Wiki</a></li>
<li><a href="/rltoken/GXZWV9hhtZN1-WnRkRSoUg" title="IETF RFC 4251 (Description of the SSH Protocol)" target="_blank">IETF RFC 4251 (Description of the SSH Protocol)</a></li>
<li><a href="/rltoken/bH7JrEiKN4Q6-J58d9pAsw" title="Internet Engineering Task Force" target="_blank">Internet Engineering Task Force</a></li>
<li><a href="/rltoken/lDe2f7hVqQPPCNr5i2zE-g" title="Request for Comments" target="_blank">Request for Comments</a></li>
</ul>

<p><strong>man or help</strong>:</p>

<ul>
<li><code>ssh</code></li>
<li><code>ssh-keygen</code></li>
<li><code>env</code></li>
</ul>