docker run \
 -p 2222:22 \
 -v ./upload:/home/a_b/upload \
 -v ./testkey.pub:/home/a_b/.ssh/keys/sftp_rsa.pub:ro \
 -d atmoz/sftp a_b::1001
