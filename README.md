# twitch-modlog

A Django project to parse and search Twitch logs to assist in moderation

## Getting Started

This project is intended to be run inside a virtualized environment, such
as a Vagrant container. Add a file called `local_settings.py` and define
at minimum a secret key, allowed hosts, and database. Run the project like
any other django site.

## Importing

The management command `import_logs` can import IRC logs in the Irssi format
with a year, month, and date in the file name. I use a command similar to the
following:

```
find /logs/ | grep -E 'scglive|scgtour' | xargs -n 1 -P 1 ./manage.py import_logs
```

You will also probably need to keep the database up to date by importing /new/
logs as your chat is used. I use a command similar to the following in my crontab:

```
find /logs/ -mtime -1 | grep -E 'scglive|scgtour' | xargs -n 1 -P 1 ./manage.py import_logs
```

## Contributing

If this is in some way useful to you, or it would be useful with minor changes,
feel free to submit a GitHub pull request.

## License

This project is licensed under the GNU General Public License, version 2,
or any later version published by the Free Software Foundation.
