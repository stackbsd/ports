--- horizon-25.7.3/openstack_dashboard/api/rest/config.py.orig	2026-10-23 09:37:49.050680000 +0000
+++ horizon-25.7.3/openstack_dashboard/api/rest/config.py	2026-10-23 09:37:49.091925000 +0000
@@ -92,6 +92,11 @@
 
     @rest_utils.ajax()
     def get(self, request):
-        zones = {tz: datetime.now(zoneinfo.ZoneInfo(tz)).strftime('%z')
-                 for tz in zoneinfo.available_timezones()}
+        zones = {}
+        for tz in zoneinfo.available_timezones():
+            # FreeBSD's Factory zone has a TZ string zoneinfo cannot parse
+            try:
+                zones[tz] = datetime.now(zoneinfo.ZoneInfo(tz)).strftime('%z')
+            except ValueError:
+                continue
         return JsonResponse({'timezone_dict': zones})
