#!/usr/bin/env python3

import sys

# pip3 install dnspython / pkg install py36-dnspython
import dns.resolver


def warn(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def find_mx(domain):
    """Returns list of MX records. If no MX records returned 'domain' returned as fallback.
    none returned on NXDOMAIN."""
    mx = []
    try:
        answer = dns.resolver.query(domain, 'MX')
    except dns.resolver.NoAnswer:
        return [domain]
    except dns.resolver.NXDOMAIN:
        return []
    except (dns.exception.Timeout, dns.resolver.NoNameservers) as e:
        # XXX we treat here temporary error as a permanent one
        # because script expected to be run several times
        warn('{}: {}'.format(domain, e))
        return []

    for rr in answer:
        mx.append(rr.exchange.to_text())
    return mx


def get_all_ip(host):
    ip_list = []
    for record_type in 'A', 'AAAA':
        try:
            for rr in dns.resolver.query(host, record_type):
                ip_list.append(rr.to_text())
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
            pass
        except dns.exception.DNSException as e:
            warn('{}: {}'.format(host, repr(e)))

    return ip_list


def get_all_mx_ip(domain):
    """Returns list of all IP addresses for all MXes."""
    mx_ip = []

    for host in find_mx(domain):
        mx_ip.extend(get_all_ip(host))

    return mx_ip


def main():
    for domain in sys.stdin:
        domain = domain.strip()

        ip_list = get_all_mx_ip(domain)
        if ip_list:
            print(domain)


if __name__ == '__main__':
    main()
