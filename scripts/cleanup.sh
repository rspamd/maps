#!/bin/sh

set -e

usage() {
	echo "usage: $0 ( resolve | merge )" >&2
	exit 1
}

[ $# -ge 1 ] || usage

command=$1

MAIL_DOMAINS=$(find freemail -name '*.txt')

case $command in
resolve)
	for _map in $MAIL_DOMAINS; do
		TS=$(date +%s)
		python3 scripts/resolve.py < "$_map" > "${_map}-${TS}"
	done
;;
merge)
	for _map in $MAIL_DOMAINS; do
		sort -u ${_map}-[0-9][0-9][0-9][0-9][0-9][0-9]* > $_map
		rm ${_map}-[0-9][0-9][0-9][0-9][0-9][0-9]*
	done
;;
*)
	usage
;;
esac
