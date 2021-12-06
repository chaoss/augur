==============
Setting up SSH
==============
In order to connect to the Amazon EC2 instance, the permissions on the .pem key-pair file need to be set correctly. This is done differently for Mac and Windows users:

Mac
===

1. Open Terminal
2. Change directory to where the key-pair is located:

 .. code-block:: bash 

    cd /path/to/keypair.pem
3. Change key-pair permissions to give the owner of the document read access and no permission to group and world. **chmod** is the command to change file permissions, and **400** are the permissions associated with the given restrictions:

 .. code-block:: bash 

    chmod 400

Windows
=======
How to set the correct permissions varies based on the command-line interface being used.This section will be split between using PowerShell or Windows Subsystem for Linux. 

`PowerShell <https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.2>`_
---------------------------------------------------------------------------------------------------
1. Open PowerShell

 .. code-block:: bash 

    cd /path/to/keypair.pem
2. Create a variable set to the location of the key-pair file

 .. code-block:: bash 

    $path = “.\key-pair.pem”
3. Reset the file to remove explicit permissions

 .. code-block:: bash 

    icacls.exe $path /reset
4. Give the current user explicit read-permission

 .. code-block:: bash 

    icacls.exe $path /GRANT:R “$($env:USERNAME):(R)”
5. Disable inheritance and remove inherited permissions

 .. code-block:: bash 

    icacls.exe $path /inheritance:r

`Windows Subsystem for Linux  <https://docs.microsoft.com/en-us/windows/wsl/install>`_
---------------------------------------------------------------------------------------
1. Open Windows Subsystem for Linux
2. Change directory to where the key-pair is located:

 .. code-block:: bash 

    cd /path/to/keypair.pem
3. Copy the key-pair file to outside of the /mnt directory

 .. code-block:: bash 

    cp keypair.pem /home
4. Change key-pair permissions to give the owner of the document read access and no permission to group and world. “chmod” is the command to change file permissions, and 400 are the permissions associated with the given restrictions:

 .. code-block:: bash 

    chmod 400

SSH into Amazon EC2 Instance
============================
1. Select the Amazon EC2 instance on the AWS console
2. Choose Connect on the instance page
3. Go to the SSH client tab
4. Copy the line that includes the key-pair name and the Public DNS:

 .. code-block:: bash 

    ssh -i “keypair.pem” ubuntu@ec2-1-23-45-67.amazonaws.com
5. Open an SSH client in the directory of the key-pair file 
6. Paste the previous line and press enter
