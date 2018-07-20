# Scripts

## How to remove domains which has no resolvable MX record

From work directory root run `scripts/cleanup.sh resolve`. Better to do it at least two times with interval several hours to not remove domains because of temporary network errors.
Then run `scripts/cleanup.sh merge`.
