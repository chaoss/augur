server {
	listen 443 ssl;
	server_name team10.guillotine.io;

	ssl_certificate /home/group10/github/augur/group10/certs/augur-snakeoil.pem;
	ssl_certificate_key /home/group10/github/augur/group10/certs/augur-snakeoil.key;
	ssl_protocols TLSv1.1 TLSv1.2 TLSv1.3;

	root /home/group10/github/augur/frontend/dist;
	index index.html index.htm;

	location / {
		root /home/group10/github/augur/frontend/dist;
		try_files $uri $uri/ /index.html;
	}

	location /api/unstable/ {
		proxy_pass https://team10.guillotine.io:5099;
		proxy_set_header Host $host;
	}

	location /api_docs/ {
		root /home/sean/github/augur-howison/frontend/public;
		index index.html;
	}

	error_log /var/log/nginx/team10.osshealth.error.log;
	access_log /var/log/nginx/team10.osshealth.access.log;	
}
