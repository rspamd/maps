# DKIM signing domains (the d= tag) used for spam or abuse (glob map).
# Matched against the d= of every DKIM signature whatever its verification
# result: a forged signature that claims a listed domain only hurts its sender.
# Each line is a lowercase ASCII/punycode glob matched against the whole
# domain: `*` matches any characters, dots included, and `?` matches at most one.
# A plain entry matches only itself, never its subdomains; use `*.example.com`
# for an abuser-owned zone that rotates subdomains. When the parent zone is
# shared (free dynamic DNS, hosting providers), list exact signing hosts and
# never glob the parent.

# DnsExit free dynamic-DNS host; German diet-pill spam from Google Cloud, Oct 2026
supportinfo.linkpc.net
