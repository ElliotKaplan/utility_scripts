#!/usr/bin/sed -f

# intended to highlight nmap script ssl-enum-ciphers for pci dss compliance

# check protocols
s/\b\(TLSv1\.[01]\|SSLv[0-9]\.[0-9]\)\b/[1m[91m\1[0m/ # TLS < 1.2 fail
s/\b\(TLSv1\.[23]\)\b/[1m[92m\1[0m/ # TLS >= 1.2 pass

# pass ciphers according to
# https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/compliance-status/
s/\b\(TLS_\(AKE_WITH_\)\?AES_128_GCM_SHA256\)\b/[1m[92m\1[0m/
s/\b\(TLS_\(AKE_WITH_\)\?AES_256_GCM_SHA384\)\b/[1m[92m\1[0m/
s/\b\(TLS_\(AKE_WITH_\)\?CHACHA20_POLY1305_SHA256\)\b/[1m[92m\1[0m/
s/\b\(TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256\)/[1m[92m\1[0m/
s/\b\(TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256\)/[1m[92m\1[0m/
s/\b\(TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384\)/[1m[92m\1[0m/
s/\b\(TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384\)/[1m[92m\1[0m/
s/\b\(TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256\)/[1m[92m\1[0m/
s/\b\(TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256\)/[1m[92m\1[0m/

# Fail all other ciphers. The color codes from passing ciphers move
# the word boundary so that the following regex will not catch them
s/\b\(TLS\(_[A-Z0-9]\+\)\+\)\b/[1m[91m\1[0m/ 

