Web Server Configuration
------------------------

Configuring nginx for Augur to run behind nginx requires you to have certain options available for symlinks and other basic nginx options. The `nginx.conf` file below is one example of a configuration known to work.

Once you have nginx configured, issue these commands to make sure everything is loaded and configured correctly:

1. sudo nginx -t to make sure its configured correctly.
	`nginx: the configuration file /etc/nginx/nginx.conf syntax is ok`
	`nginx: configuration file /etc/nginx/nginx.conf test is successful`
2. sudo systemctl restart nginx (ubuntu)
3. sudo nginx (OSX)

------------------
Server Compilation
------------------

Your Augur instance must be compiled with publicly accessible domain that the front end instance will be able to access.

1. As a practical matter, set your `augur.config.json` server block like this:

.. code-block:: json

	{
	    "Server": {
	        "cache_expire": 3600,
	        "host": "subdomain.domain.tld",
	        "port": "5000",
	        "workers": 8
	    }
    }

2.   Compile augur (this wires the host and port into the front end so people pulling the web pages of Augur, in the `frontend/` subdirectory are referring to the right endpoints for this instance.): `make rebuild`
3.   Run Augur: `nohup augur backend start >augur.log 2>augur.err &`


------------------
nginx
------------------

------------------
nginx.conf
------------------

.. code-block::

	user www-data;
	worker_processes auto;
	pid /run/nginx.pid;
	include /etc/nginx/modules-enabled/*.conf;

	worker_rlimit_nofile 30000;

	events {
		worker_connections 768;
		# multi_accept on;
	}

	http {

		##
		# Basic Settings
		##
		disable_symlinks off;

		sendfile on;
		tcp_nopush on;
		tcp_nodelay on;
		keepalive_timeout 65;
		types_hash_max_size 2048;
		# server_tokens off;

		 server_names_hash_bucket_size 64;
		# server_name_in_redirect off;

		include /etc/nginx/mime.types;
		default_type application/octet-stream;

		##
		# SSL Settings
		##

		ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3; # Dropping SSLv3, ref: POODLE
		ssl_prefer_server_ciphers on;

		##
		# Logging Settings
		##

		access_log /var/log/nginx/access.log;
		error_log /var/log/nginx/error.log;

		##
		# Gzip Settings
		##

		gzip on;

		# gzip_vary on;
		# gzip_proxied any;
		# gzip_comp_level 6;
		# gzip_buffers 16 8k;
		# gzip_http_version 1.1;
		# gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

		##
		# Virtual Host Configs
		##

		include /etc/nginx/conf.d/*.conf;
		include /etc/nginx/sites-enabled/*;
	}

--------------------
Site Configuration
--------------------

This file will be located in your `/etc/nginx/sites-enabled` directory on most linux distributions.  Mac OSX keeps these files in `/usr/local/etc/nginx/sites-enabled` **Note that Augur's backend server must be running**

.. code-block::

		server {
		        listen 80;
		        server_name  <<your server subdomain.domain.tld>>;

		        root /home/user/.../<<augur-instance-home>>/frontend/dist;
		        index index.html index.htm;

		        location / {
		        root /home/user/.../<<augur-instance-home>>/frontend/dist;
		        try_files $uri $uri/ /index.html;
		        }

		#        location /api/unstable/ {
		#                proxy_pass http://census.osshealth.io:5000;
		#                proxy_set_header Host $host;
		#        }

		        location /api_docs/ {
		        root /home/user/.../<<augur-instance-home>>/frontend/dist;
		        index index.html;
		        }


		        error_log /var/log/nginx/augur.censusscienceosshealth.error.log;
		        access_log /var/log/nginx/augur.censusscienceosshealth.access.log;

		}
		
--------------------
HTTPS
--------------------

HTTPS is an extension of HTTP. It is used for secure communication over a computer network and it is important that your deployment utilizes HTTPS. 
A possible error that is encountered when not using HTTPS is the **Mixed Content** error which blocks communication between your page and the server.

To convert from HTTP to HTTPS the `/insert/path/to/file(s)/where/the/issue/is` must be set up as follows:

.. code-block::

		placeholder {
		        placeholder;
		        place_holder  <<place.holder.text>>;
			$placeholder



		#        location /api/unstable/ {
		#                proxy_pass http://dev.osshealth.io:5000;
		#                proxy_set_header Host $host;
		#        }

		        placeholder /placeholder/ {
		        placeholder /placeholder/placeholder/.../<<placeholder>>/placeholder/placeholder;
		        index index.html;
		        }


		        error_log /var/log/nginx/placeholder.error.log;
		        access_log /var/log/nginx/augur.placeholder.access.log;

		}


**FOR GROUP 11, WE WILL MODIFY THE ABOVE CODE BLOCK, ONCE THE SOLUTION IS FOUND SEND IT TO ADAM AND HE WILL UPDATE THIS DOCUMENTATION**		
