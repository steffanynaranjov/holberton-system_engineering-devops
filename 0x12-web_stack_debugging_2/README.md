<h1 class="gap">0x12. Web stack debugging #2</h1>

   <h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>All your files will be interpreted on Ubuntu 14.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A README.md file at the root of the folder of the project is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>Your Bash scripts must pass <code>Shellcheck</code> without any error</li>
<li>Your Bash scripts must run without error</li>
<li>The first line of all your Bash scripts should be exactly #!/usr/bin/env bash</li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
</ul>


  <h4 class="task">
    0. Run software as another user
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  <p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/eaeff07a715ff880b1ceb8e863a1d141a74a7f85.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210104%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210104T133228Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9c50ce5fbca1c514677d314979b3ff6778a37ed9ac45b38c3648ec821b1de3e0" alt="" style="" /></p>

<p>The user <code>root</code> is, on Linux, the &ldquo;superuser&rdquo;. It can do anything it wants, that&rsquo;s a good and bad thing. A good practice is that one should never be logged in the <code>root</code> user, as if you fat finger a command and for example run <code>rm -rf /</code>, there is no comeback. That&rsquo;s why it is preferable to run as a privileged user, meaning that the user also has the ability to perform tasks that the <code>root</code> user can do, just need to use a specific command that you need to discover.</p>

<p>For the containers that you are given in this project as well as the checker, everything is run under the <code>root</code> user, which has the ability to run anything as another user.</p>
