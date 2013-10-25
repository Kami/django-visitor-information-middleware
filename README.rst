Django Visitor Information Middleware
=====================================

This module contains a collection of middleware classes which make writing
timezone and location aware applications easier.

Information provided by this middleware can be used to do things like:

* Display a cookie consent message if visitor is coming from the country
  within the EU
* Display timezone change notification if a user's location timezone doesn't
  match a timezone which is currently set in the profile
* ...

Installation
------------

.. sourcecode:: bash

    pip install django-visitor-information-middleware

Geolocation Database
--------------------

To determine location information based on the user IP address, this module
uses GEO IP database.

By default, it ships with a free GeoLite2 database
(http://dev.maxmind.com/geoip/geoip2/geolite2/).

If you want to use a custom database file, simply set
``VISITOR_INFO_GEOIP_DATABASE_PATH`` setting to point to your geoip database
file. Keep in mind that this file needs to be readable by a process under
which your Django application is running.

Included Middleware
-------------------

TimezoneMiddleware
~~~~~~~~~~~~~~~~~~

The middleware activates a timezone for an authenticated user.

VisitorInformationMiddleware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This middleware adds the following keys to the ``request.visitor`` dictionary:

* ``country`` - country the visitor is based in
* ``city`` - city the visitor is based in
* ``location.timezone`` - timezone used in the location visitor is based in
* ``location.unit_system`` - unit system used in the location visitor is based
  in
* ``user.timezone`` - timezone of the currently authenticated user
* ``user.unit_system`` - unit system of the currently authenticated user.
* ``cookie_notice`` - True if a cookie consent notice should be displayed for
  the current visitor.

Note: Location of the user is determined based on the user's IP address.
