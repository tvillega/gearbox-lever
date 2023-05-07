![logo](logo.png)

Terminal utility to manage Transmission BitTorrent Client.

> Currently not on a working stage

## Observations

It seems that the python library [transmission-rpc](https://pypi.org/project/transmission-rpc/) does not cover all API calls, so I'll use cURL instead. However, making jsonrpc requests with bash has the downside of escaping \".

I'm currently exploring the possibility of making such calls inside a perl script, putting the jsonrpc request inside a perl's dictionary and then only calling the variable. This would make me drop the python language and replace it with perl.

## Environment

Clone the repo
```
$ git clone git@github.com:tvillega/gearbox-lever.git
```

Create python environment:
```
$ cd gearbox-lever
$ python -m venv .env
$ . .env/bin/activate
(.env) $ pip install transmission-rpc
```
