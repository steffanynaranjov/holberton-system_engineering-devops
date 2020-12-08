#SSH configuration file so that you can connect to a server without
# typing a password.
file_line { '/etc/ssh/ssh_config':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no;    IdentityFile ~/.ssh/holberton',
}
