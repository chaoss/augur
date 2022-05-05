Example Amazon EC2 Launch
-------------------------

------
Steps
------
1. Open AWS Console

.. image:: ../development-guide/images/AWSManagementConsole.png
  :width: 700
  :alt: AWS Management Console

2. Navigate to the EC2 Management Console using the search bar
3. Launch Instance

.. image:: ../development-guide/images/LaunchInstance.png
  :width: 700
  :alt: AWS Launch EC2 Instance

4. Browse more AMIs
	- Select Ubuntu 20.04 and leave the setting on 64bit (x86)

.. image:: ../development-guide/images/Ubuntu.png
  :width: 700
  :alt: Select Ubuntu for EC2 Type

5. Change the instance type to t2.medium
6. Create a key pair and save it in a safe location
7. Under Network Settings
	- Enable “Allow HTTPs traffic from the internet”
	- Enable “Allow HTTP traffic from the internet”
	- Click Edit
		- Open Port 5432 for postgres
		- Open Port 5000 for augur
8. Configure Storage
	- Change 8 GiB to 30 GiB
