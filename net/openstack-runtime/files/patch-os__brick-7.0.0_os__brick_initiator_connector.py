# Look up the os-brick-freebsd connectors on FreeBSD

--- os_brick-7.0.0/os_brick/initiator/connector.py.orig	2026-11-17 09:06:43.101789551 +0000
+++ os_brick-7.0.0/os_brick/initiator/connector.py	2026-11-17 09:06:58.959098645 +0000
@@ -34,6 +34,11 @@
 
 LOG = logging.getLogger(__name__)
 
+try:
+    from os_brick_freebsd import CONNECTORS as freebsd_connectors
+except ImportError:
+    freebsd_connectors = {}
+
 unix_connector_list = [
     'os_brick.initiator.connectors.base.BaseLinuxConnector',
     'os_brick.initiator.connectors.iscsi.ISCSIConnector',
@@ -56,6 +61,8 @@
 
 
 def _get_connector_list():
+    if sys.platform.startswith('freebsd'):
+        return unix_connector_list + list(freebsd_connectors.values())
     return unix_connector_list
 
 
@@ -146,8 +153,7 @@
 # TODO(smcginnis) Remove this lookup once unit test code is updated to
 # point to the correct location
 def _set_aliases():
-    conn_list = _get_connector_list()
-    for item in conn_list:
+    for item in unix_connector_list:
         _name = item.split('.')[-1]
         globals()[_name] = importutils.import_class(item)
 
@@ -217,6 +223,9 @@
     if arch is None:
         arch = platform.machine()
 
+    if sys.platform.startswith('freebsd'):
+        return {**_connector_mapping_linux, **freebsd_connectors}
+
     # Set the correct mapping for imports
     if arch in (initiator.S390, initiator.S390X):
         return _connector_mapping_linux_s390x
